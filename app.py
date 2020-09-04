from flask import Flask,render_template,request
import pickle
import pickle,joblib
model=pickle.load(open('Attrition.pkl','rb'))
trans=joblib.load('transform.save')
app=Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/login',methods=["POST"])
def func2():
    Education=request.form['Education']
    JobInvolvement=request.form['JobInvolvement']
    JobLevel=request.form['JobLevel']
    DailyRate=request.form['DailyRate']
    MonthlyIncome=request.form['MonthlyIncome']
    NoofCompaniesWorked=request.form['NoofCompaniesWorked']
    TotalWorkingYears=request.form['TotalWorkingYears']
    YearsAtCompany=request.form['YearsAtCompany']
    YearsInCurrentRole=request.form['YearsInCurrentRole']
    YearsSinceLastPromotion=request.form['YearsSinceLastPromotion']
    YearsWithCurrentManager=request.form['YearsWithCurrentManager']
    TrainingTimesLastYear=request.form['TrainingTimesLastYear']
    PerformanceRating=request.form['PerformanceRating']
    data=[[int(Education),int(JobInvolvement),int(JobLevel),int(DailyRate),int(MonthlyIncome),int(NoofCompaniesWorked),int(TotalWorkingYears),int(YearsAtCompany),int(YearsInCurrentRole),int(YearsSinceLastPromotion),int(YearsWithCurrentManager),int(TrainingTimesLastYear),int(PerformanceRating)]]
    output= trans.transform(data)
    pred=model.predict(output)
    print(pred[0])
    if(pred==0):
        ans='Employee will stay'
    else:
        ans ='Employee will be terminated'
    return render_template("index.html",y=ans)
if __name__=='__main__':
   app.run(debug= True)