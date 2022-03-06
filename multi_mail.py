import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 
from datetime import datetime
import time



#The mail addresses and  password
sender_address ='sufyan1232@gmail.com'              
sender_pass = 'kjbkwdfuxeuzpusi'                              

# list of reciver email_id to the mail 
li = ['creativelab999@gmail.com']                   
                                      
#[item for item in input("Enter Receiver Mail Address :- ").split()] this is used to take user input of receiver mail id

# getting length of list 
length = len(li) 
   

mail_count = 0

for i in range(length): 
    print("Starting email sending")
    mail_count += 1
    # print(i%10)
    
    if i%10==0 and i!=0:
        print("sleeping for 5 seconds")
        time.sleep(5)
    else:
        pass    
    X = li[i]
    reciver_mail = X
    
    # print(reciver_mail)
    # print("Mail Sent Time ------>>>>>", current_time)
    
    try:
        
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] =  reciver_mail             #  Pass Receiver Mail Address
        message['Subject'] =  'CV for the post of Dev-Ops Software Developer / Assistant Manager / Database Architect'       #The subject line
        

        mail_content ='''
        
        Hello, 
        
        I am a Skilled Dev-Ops Software Developer /Assistant manager with experience in Database and supply chain consultancy. As a assistant manager at Safexpress pvt ltd I have designed,
        tested and deployed Project/ ML Models/Applications/DB implementation and numerous other projects.
        I also possess a very Strong Fucntional knowledge of the entire Logistics & supply chain workflow from First Mile to Last Mile.
        Single-handedly on-boarded & integrated 100+ customers of Safexpress which resulted in saving lakhs of
        rupees and extra man hours.
        
        
        
        My Key skills include :
        
        Dev-Ops| Data-Set building | Process improvement | Cross-functional Co-ordination |Cost Reduction |  Data analytics
        | Predictive Modeling | Excellent Logical,analytical & problem solving |Data Integration | Supply-Chain
        
        
        
        My technical skills include :
        
        AWS (EC2 , S3 , RDS , ECS , CloudWatch , Lambda , SES) | Docker| Python | Oracle SQL| PostgreSQL 
        | BI Publisher | Linux | CI/CD | Google Notebook | EMR | PySpark | Hadoop | Terraform| Kubernetes | 
        Jenkins | Ansible | Git | CloudFormation | VPC | 
        
        I have attached my CV with this E-mail.
        Kindly revert in case of any requirement.

        Regards,
        Sufyan Ahmed
        +91 7208659644
        Delhi India 
        '''

        
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))

        filename = 'Sufyan_cv_22.pdf'
        
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part) 

        part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

        message.attach(part) 


        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(sender_address, sender_pass) 
        text = message.as_string()
        s.sendmail(sender_address, reciver_mail, text) 
        s.quit()

        now = datetime.now()
        
        current_time = now.strftime("%H:%M:%S")
        
        
        print('CV & E-Mail Sent to    ------>>>>>>     '+ X + '     at ', current_time)
        
        print(mail_count)
        
    
    except Exception as e:
        print(e)
        pass
