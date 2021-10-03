from flask import Flask,render_template,request
import csv
app=Flask(__name__)
@app.route('/')
def home ():
   return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
   return  render_template(page_name)

'''
@app.route('/works.html')
def blog():
	return  render_template('works.html')

@app.route('/about.html')
def about1():
    return render_template("about.html")    




@app.route('/contact.html')
def about2():
    return render_template("contact.html") 

@app.route('/components.html')
def about3():
    return render_template("components.html") 
    '''  


 
 

def wr_to_csv(data):
    with open("database.csv",newline='',mode='a') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer =  csv.writer(database2)
        #file=database2.writerow(database2,delimeter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])  
        #file=database2.writerow(f'\n mail, sub, msg \n{email},{subject},{message}') 

def write(data):
  with open ('database.txt',mode='a')as database:
      email=data["email"]
      subject=data['subject']
      message=data['message']
      file=database.write(f'\n  mail:{email},\nsub:{subject},\nmsg:{message}')  
@app.route('/submit form',methods=['POST','GET'])
def submit_form():
   if request.method=='POST':
     data=request.form.to_dict()
     write(data)
     wr_to_csv(data)
     print(data)
     return 'FORM SUBMITTED'
   else:
      return 'not submitted'  





if __name__=='__main__':
    app.run(debug=True)
