import numpy as np


class Precise:
    def __init__(self, y_true, y_pred):
        self.__y_true = y_true
        self.__y_pred = y_pred

    @staticmethod
    def mean_absolute_percentage_error(y_tr, y_pr):
        """
        Calculate the mean absolute percentage error (MAPE).
        """
        y_tr, y_pr = np.array(y_tr), np.array(y_pr)
        return np.mean(np.abs((y_tr - y_pr) / y_tr)) * 100

    @staticmethod
    def root_mean_square_error(y_tr, y_pr):
        """
        Calculate the root mean square error (RMSE).
        """
        y_tr, y_pr = np.array(y_tr), np.array(y_pr)
        return np.sqrt(np.mean((y_tr - y_pr) ** 2))

    @staticmethod
    def mean_absolute_error(y_tr, y_pr):
        """
        Calculate the mean absolute error (MAE).
        """
        y_tr, y_pr= np.array(y_tr), np.array(y_pr)
        return np.mean(np.abs(y_tr - y_pr))

    @staticmethod
    def coefficient_of_determination(y_tr, y_pr):
        """
        Calculate the coefficient of determination (R-squared).
        """
        y_tr, y_pr = np.array(y_tr), np.array(y_pr)
        ss_total = np.sum((y_tr - np.mean(y_tr)) ** 2)
        ss_residual = np.sum((y_tr - y_pr) ** 2)
        r_squared = 1 - (ss_residual / ss_total)
        return r_squared

    @staticmethod
    def mean_error(self, y_true, y_pred):
        """
        Calculate the mean error (ME).
        """
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        return np.mean(y_true - y_pred)

    def gety_true(self):
        return self.__y_true

    def gety_pred(self):
        return self.__y_pred


    def performance(self):
        perf_indicators=dict()
        perf_indicators["rmse"] = self.root_mean_square_error(self.__y_true,self.__y_pred)
        perf_indicators["mape"] = self.mean_absolute_percentage_error(self.__y_true,self.__y_pred)
        perf_indicators["MAE"] = self.mean_absolute_error(self.__y_true,self.__y_pred)
        perf_indicators["Coef_det"] = self.coefficient_of_determination(self.__y_true,self.__y_pred)


        return perf_indicators