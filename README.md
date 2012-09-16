#Linear Regression Implementation in Python

Some Theory - Linear Regression problem comes under Supervised Learning, in which you try to predict some real value output on the basis of historical data.

The Model uses Gradient descent algorithm, which uses partial derivative of cost function to find some values of Q0,Q1,....,Qn

Consider you have a job site such as shine.com, naukri.com, etc.
These have historical data of each employee - Employee1 have done btech from college ABC, have speciality in Java, have 2yrs of experience and wants a job with $30,000 a month
We can use this historical data to train our model and
1. Predict salary for new employees
2. Guiding students properly to take better career path
3. Finding Market Trends

##Algorithm -

Assumption -Let, function J(Q0,Q1,....,Qn)

Aim - To find minJ(Q0,Q1,....,Qn)

- Begin with any value Q0, Q1, ...., Qn
- Keep changing values of Q0,Q1,....,Qn to reduce J(Q0,Q1,....,Qn), until we find min J(Q0,Q1,....,Qn)

##How It Works

Add your training data in dictionary TRAINING_DATA present in file training_data.py

Add your new data in dictionary PREDICTION_DATA present in file training_data.py

Learning rate is represented bt a

Run Command - python linear-regression.py

##TROUBLESHOOTING -

If you are getting new values of Q0, Q1,...., Qn positive and negative alternatively. Try, reducing Learning rate 'a' present in file training_data.py


