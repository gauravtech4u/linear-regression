
BRANCH_DICT={'cs':80,'it':60,'ec':60,'ee':40,'me':40}

COURSE_DICT={'java':60,'.net':60,'python':70,'scala':80,'haskel':80,'ruby':75,'c':60,'c++':60}

FEATURE_MAPPING={1:'high school score',2:'board score',3:'graduation score',4:'graduation years',5:'branch',6:'courses done',7:'salary grade'}

GRADE_DICT={'$4000 a month':(2000,2500), '$4000 a month':(1500,2000),'$3000 a month':(1000,1500),'$2500 a month':(500,1000)}

FEATURES_DICT={
    0:1,
    1:100,
    2:100,
    3:100,
    4:5,
    5:BRANCH_DICT,
    6:COURSE_DICT,
    7:None
}

TRAINING_DATA=[
    [1,70,60,65,4,['cs'],['java','.net']],
    [1,60,80,70,4,['ee'],['c']],
    [1,80,75,80,4,['ec'],['c']],
    [1,50,55,60,5,['cs'],['ruby']],
    [1,70,60,75,4,['me','it'],['c','python','ruby']],
    [1,80,70,65,4,['me'],['python','java']],
    [1,50,50,65,5,['me'],['.net']],
]

# score for each row in Training matrix
Y =[1200.00,1000.00,1100.00,1000.00,900.00,2100.00,700.00]

# PREDICTION_DATA - Data whose score needs to be computed, Last element in each row represents its score
PREDICTION_DATA=[
    [1,60,60,55,4,['cs'],['java','.net'],None],
    [1,70,75,65,4,['ee'],['c'],None],
    [1,60,55,55,4,['ee'],[],None],
    [1,70,80,70,4,['ec'],['c'],None],
    [1,60,50,55,5,['cs'],['ruby'],None],
    [1,80,70,60,4,['me'],['python','ruby'],None],
    [1,60,50,50,4,['me','cs'],['python'],None],
    [1,80,90,80,7,['cs','ec'],['python','ruby','java'],None],
]

QT=[8.00,1.00,5.00,3.00,10.00,7.00,1.00]


# Feature Conversion Begins

def convert_data(TEMP_DICT={}):
    for i,data in enumerate(TEMP_DICT):
             for j,weight in enumerate(data):
                     if type(weight) == type([]):
                         sum=0
                         for ele in weight:
                            sum+= FEATURES_DICT[j][ele]
                         TEMP_DICT[i][j]=sum
    return TEMP_DICT


TRAINING_DATA=convert_data(TRAINING_DATA)

PREDICTION_DATA=convert_data(PREDICTION_DATA)

# Feature Conversion Ends


CONVERGE_LIMIT=20000

# Learning Rate
a=0.00000001

m=len(TRAINING_DATA)

n=len(PREDICTION_DATA)

print "Features Considered ->"
print FEATURE_MAPPING.values()[:-1]