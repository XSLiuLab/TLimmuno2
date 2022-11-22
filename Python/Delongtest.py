import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as st
from sklearn import metrics

class DelongTest():
    def __init__(self,preds1,preds2,label,threshold=0.05):
        '''
        preds1:the output of model1
        preds2:the output of model2
        label :the actual label
        '''
        self._preds1=preds1
        self._preds2=preds2
        self._label=label
        self.threshold=threshold
        self.show_result()

    def _auc(self,X, Y)->float:
        return 1/(len(X)*len(Y)) * sum([self._kernel(x, y) for x in X for y in Y])

    def _kernel(self,X, Y)->float:
        '''
        Mann-Whitney statistic
        '''
        return .5 if Y==X else int(Y < X)

    def _structural_components(self,X, Y)->list:
        V10 = [1/len(Y) * sum([self._kernel(x, y) for y in Y]) for x in X]
        V01 = [1/len(X) * sum([self._kernel(x, y) for x in X]) for y in Y]
        return V10, V01

    def _get_S_entry(self,V_A, V_B, auc_A, auc_B)->float:
        return 1/(len(V_A)-1) * sum([(a-auc_A)*(b-auc_B) for a,b in zip(V_A, V_B)])
    
    def _z_score(self,var_A, var_B, covar_AB, auc_A, auc_B):
        return (auc_A - auc_B)/((var_A + var_B - 2*covar_AB )**(.5)+ 1e-8)

    def _group_preds_by_label(self,preds, actual)->list:
        X = [p for (p, a) in zip(preds, actual) if a]
        Y = [p for (p, a) in zip(preds, actual) if not a]
        return X, Y

    def compute_z_p(self):
        X_A, Y_A = self._group_preds_by_label(self._preds1, self._label)
        X_B, Y_B = self._group_preds_by_label(self._preds2, self._label)

        V_A10, V_A01 = self._structural_components(X_A, Y_A)
        V_B10, V_B01 = self._structural_components(X_B, Y_B)

        auc_A = self._auc(X_A, Y_A)
        auc_B = self._auc(X_B, Y_B)

        # Compute entries of covariance matrix S (covar_AB = covar_BA)
        var_A = (self._get_S_entry(V_A10, V_A10, auc_A, auc_A) * 1/len(V_A10)+ self._get_S_entry(V_A01, V_A01, auc_A, auc_A) * 1/len(V_A01))
        var_B = (self._get_S_entry(V_B10, V_B10, auc_B, auc_B) * 1/len(V_B10)+ self._get_S_entry(V_B01, V_B01, auc_B, auc_B) * 1/len(V_B01))
        covar_AB = (self._get_S_entry(V_A10, V_B10, auc_A, auc_B) * 1/len(V_A10)+ self._get_S_entry(V_A01, V_B01, auc_A, auc_B) * 1/len(V_A01))

        # Two tailed test
        z = self._z_score(var_A, var_B, covar_AB, auc_A, auc_B)
        p = st.norm.sf(abs(z))*2

        return z,p

    def show_result(self):
        z,p=self.compute_z_p()
        return z,p
        #print(f"z score = {z:.5f};\np value = {p:.5f};")
        #if p < self.threshold :print("There is a significant difference")
        #else:        print("There is NO significant difference")
