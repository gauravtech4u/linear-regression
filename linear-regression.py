from training_data import *

"""
    Gradient Descent for multiple features

    Hypothesis      - h(X)= QT^T*X = QT0 * X0 + QT1 * X1 + QT2 * X2+ .... + Qn * Xn

    Cost Function   - J(Q) = 1/2m *( (h(X)^(0) - y^(0))^2 + (h(X)^(1) - y^(1))^2 + .... + (h(X)^(m) - y^(m))^2 )

    Gradient Descent Algorithm -

    repeat {

        Qj  =   Qj - a * d( J(Q0,Q1,....,qn))/dQj

            =   Qj - a * 1/m (( h(x)^(0) - y^(0))*x^(0) + .... + ( h(x)^(m) - y^(m))*x^(m))

    }

    here, x0^(i) = 1


"""


class LinearRegression(object):

    def converge(self):
        QTX=QT
        x=0
        while x < CONVERGE_LIMIT:
                QTX_LIST=QTX
                for q in range(len(QTX_LIST)):
                    for i in range(m):
                        matrix_sum,temp_sum=0.0,0.0
                        for k in range(len(QTX_LIST)):
                            matrix_sum+=QTX_LIST[k]*TRAINING_DATA[i][k]
                        for k in range(len(QTX_LIST)):
                            temp_sum+=(matrix_sum-Y[i])*TRAINING_DATA[i][k]
                    QTX_LIST[q]-=(temp_sum*a)/float(m)
                QTX=QTX_LIST
                x+=1

        for i in range(n):
            matrix_sum=0
            for j in range(len(QTX)):
                matrix_sum+=QTX[j]*PREDICTION_DATA[i][j]
            PREDICTION_DATA[i][-1]=matrix_sum

        for grade,score_range in GRADE_DICT.items():
            for i,score in enumerate(map(lambda score:score[-1],PREDICTION_DATA)):
                if score > score_range[0] and score < score_range[1]:
                    PREDICTION_DATA[i][-1]=grade
        print PREDICTION_DATA

if __name__ == "__main__":
    regression_obj=LinearRegression()
    regression_obj.converge()



