from tkinter import *
import pyttsx3
from tkinter import ttk
from PIL import Image,ImageTk
from sklearn.svm import SVC
from ttkthemes import themed_tk
import numpy as np
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tkinter import messagebox 


class Heart:
    def __init__(self,win):
        self.win=win
        self.win.geometry('1350x800')
        self.win.title('HEART DISEASEPREDICTION SYSTEM')
        self.win.iconbitmap('heart.ico')
        self.win.resizable(False,True)
        self.text_f=Label(self.win,text='HEART DISEASE PREDICTION SYSTEM',font='cambria 50 bold',fg='red')
        self.text_f.pack()
        self.fram=Frame(self.win,bg='black')
        self.fram.place(x=80,y=80,width=1250,height=600)
        
        self.frame=Frame(self.fram,bg='white',bd=9)
        self.frame.place(x=10,y=20,width=600,height=500)
        
        self.frame2=Frame(self.fram,bg='white')
        self.frame2.place(x=620,y=20,width=600,height=500)
     
        #axis 1 
        self.id_num_label=Label(self.frame,text="Enter Patient's ID:",bg='white',fg='black',font='arial 12 bold')
        self.id_num_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)
        
        self.id_num_value=StringVar()
        self.id_num=ttk.Entry(self.frame,textvariable=self.id_num_value)
        self.id_num.grid(row=0,column=1,pady=3)
        
        self.name_label=Label(self.frame,text='Enter Name:',bg='white',fg='black',font='arial 12 bold')
        self.name_label.grid(row=1,column=0,padx=10,pady=2,sticky=W)
        
        self.name_value=StringVar()
        self.name=ttk.Entry(self.frame,textvariable=self.name_value)
        self.name.grid(row=1,column=1,pady=3)
        
        self.age_label=Label(self.frame,text='Enter your age:',bg='white',fg='black',font='arial 12 bold')
        self.age_label.grid(row=2,column=0,padx=10,pady=2,sticky=W)
        
        self.age_value=StringVar()
        self.age=ttk.Entry(self.frame,textvariable=self.age_value)
        self.age.grid(row=2,column=1,pady=3)
        
        self.sex_label=Label(self.frame,text='Choose sex:',bg='white',fg='black',font='arial 12 bold')
        self.sex_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)
        
        self.sex_value=StringVar()
        self.sex=ttk.Combobox(self.frame,textvariable=self.sex_value,state='readonly',width=18)
        self.sex['values']=('choose sex','male','female')
        self.sex.current(0)
        self.sex.grid(row=3,column=1,pady=3)
        
        self.chest_label=Label(self.frame,text='Do you feel severe chest pain:',bg='white',fg='black',font='arial 12 bold')
        self.chest_label.grid(row=4,column=0,padx=10,pady=2,sticky=W)
        
        self.chest_value=StringVar()
        self.chest=ttk.Combobox(self.frame,textvariable=self.chest_value,state='readonly',width=18)
        self.chest['values']=('No','yes','Yes not too severe','Very severe')
        self.chest.current(0)
        self.chest.grid(row=4,column=1,pady=3,sticky=W)
        
        self.restingBP_value=StringVar()
        self.restingBP=Label(self.frame,text='Enter your Resting Blood Pressure level (mm Hg):',font='arial 12 bold',bg='white',fg='black')
        self.restingBP.grid(row=5,column=0,padx=10,pady=2,sticky=W)
        self.restingBP_val=ttk.Entry(self.frame,textvariable=self.restingBP_value)
        self.restingBP_val.grid(row=5,column=1,pady=3)
      
        self.chol_value=StringVar()
        self.cholestrol=Label(self.frame,text='Enter Cholestrol level (Mg/dl):',font='arial 12 bold',bg='white',fg='black')
        self.cholestrol.grid(row=6,column=0,padx=10,pady=2,sticky=W)
        self.chol_val=ttk.Entry(self.frame,textvariable=self.chol_value)
        self.chol_val.grid(row=6,column=1,pady=3)
        
        self.fastBS_value=StringVar()
        self.fastBS=Label(self.frame,text='is your sugar level greater than 120mg/dl:',font='arial 12 bold',bg='white',fg='black')
        self.fastBS.grid(row=7,column=0,padx=10,pady=2,sticky=W)
        self.fastBS_val=ttk.Combobox(self.frame,textvariable=self.fastBS_value,state='readonly',width=18)
        self.fastBS_val['values']=['Yes','No']
        self.fastBS_val.current(0)
        self.fastBS_val.grid(row=7,column=1,pady=3)
        
        
        #axis 2 
        self.ecg_label=Label(self.frame2,text='Select your ECG range:',bg='white',fg='black',font='arial 12 bold')
        self.ecg_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)
        
        self.ecg_value=StringVar()
        self.ecg=ttk.Combobox(self.frame2,textvariable=self.ecg_value,width=18,state='readonly')
        self.ecg['values']=('Choose range','Normal[-0.5 to 0.4]','ST-T Abnormal[2.45 to 1.8]','Hypertrophy[1.4 to 2.8]')
        self.ecg.current(0)
        self.ecg.grid(row=0,column=1,pady=3)
        
        
        self.heart_rate_label=Label(self.frame2,text='Enter Max. heart rate:',bg='white',fg='black',font='arial 12 bold')
        self.heart_rate_label.grid(row=1,column=0,padx=10,pady=2,sticky=W)
    
        self.heart_rate_value=StringVar()
        self.heart_rate=ttk.Entry(self.frame2,textvariable=self.heart_rate_value)
        self.heart_rate.grid(row=1,column=1,pady=3)
        
        self.induced_cp_label=Label(self.frame2,text='feeling severe chest pain after execise:',bg='white',fg='black',font='arial 12 bold')
        self.induced_cp_label.grid(row=2,column=0,padx=10,pady=2,sticky=W)
       
        self.induced_cp_value=StringVar()
        self.induced_cp=ttk.Combobox(self.frame2,textvariable=self.induced_cp_value,state='readonly',width=18)
        self.induced_cp['values']=('yes','No')
        self.induced_cp.current(0)
        self.induced_cp.grid(row=2,column=1,pady=3)
        
        self.peak_label=Label(self.frame2,text='Depression Level after exercise relative to rest:',bg='white',fg='black',font='arial 12 bold')
        self.peak_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)
     
        self.peak_value=StringVar()
        self.peak=ttk.Entry(self.frame2,textvariable=self.peak_value)
        self.peak.grid(row=3,column=1,pady=3,sticky=W)
       
        self.slope_value=StringVar()
        self.slope=Label(self.frame2,text='select slope shape:',font='arail 12 bold',bg='white',fg='black')
        self.slope.grid(row=4,column=0,padx=10,pady=2,sticky=W)
        self.slope_val=ttk.Combobox(self.frame2,textvariable=self.slope_value,state='readonly',width=18)
        self.slope_val['values']=('Up sloping','Flat','Down sloping')
        self.slope_val.current(0)
        self.slope_val.grid(row=4,column=1,pady=3)
     
        self.ca_value=StringVar()
        self.ca=Label(self.frame2,text='select Number of Major vessels:',font='arial 12 bold',bg='white',fg='black')
        self.ca.grid(row=5,column=0,padx=10,pady=2,sticky=W)
        self.ca_val=ttk.Combobox(self.frame2,textvariable=self.ca_value,state='readonly',width=18)
        self.ca_val['values']=['0','1','2','3']
        self.ca_val.current(0)
        self.ca_val.grid(row=5,column=1,pady=3)
    
        self.defect_value=StringVar()
        self.defect=Label(self.frame2,text='slect defect type:',font='arail 12 bold',bg='white',fg='black')
        self.defect.grid(row=6,column=0,padx=10,pady=2,sticky=W)
        self.defect_val=ttk.Combobox(self.frame2,textvariable=self.defect_value,state='readonly',width=18)
        self.defect_val['values']=['Normal','Fixed defect','Reversible defect']
        self.defect_val.current(0)
        self.defect_val.grid(row=6,column=1,pady=3)
        
        
        self.btn=ttk.Button(self.win,text='VIEW RESULT',width=50,command=self.prediction)
        self.btn.place(x=500,y=610)
        
        
        self.fram3=Frame(self.win,bg='black')
        self.fram3.place(x=80,y=640,width=1250,height=40)
        
        
        self.result_label=Label(self.fram3,text='',font='Tahoma 15 bold',fg='green',bg='black')
        self.result_label.pack()
        
        
        
        
        
        
    
    
    def prediction(self):
    
        if self.sex_value.get()=='male':
            self.sex_value.set('1')
        elif self.sex_value.get()=='female':
            self.sex_value.set('2')
        else:
            self.sex_value.set(random.randrange(0, 2))
        if self.chest_value.get()=='No':
            self.chest_value.set('0')
        elif self.chest_value.get()=='yes':
            self.chest_value.set('1')
        elif self.chest_value.get()=='Yes not too severe':
            self.chest_value.set('2')
        elif self.chest_value.get()=='Very severe':
            self.chest_value.set('3')
        if self.fastBS_value.get()=='Yes':
            self.fastBS_value.set('1')
        if self.fastBS_value.get()=='No':
            self.fastBS_value.set('0')
        if self.ecg_value.get()=='Normal[-0.5 to 0.4]':
            self.ecg_value.set('0')
        elif self.ecg_value.get()=='ST-T Abnormal[2.45 to 1.8]':
            self.ecg_value.set('1')
        elif self.ecg_value.get()=='Hypertrophy[1.4 to 2.8]':
            self.ecg_value.set('2')
        if self.ecg_value.get()=='Choose range':
            self.ecg_value.set(random.randrange(0,3))
        if self.induced_cp_value.get()=='yes':
            self.induced_cp_value.set('1')
        if self.induced_cp_value.get()=='No':
            self.induced_cp_value.set('0')
        if self.slope_value.get()=='Up sloping':
                self.slope_value.set('0')
        elif self.slope_value.get()=='Flat':
            self.slope_value.set('1')
        elif self.slope_value.get()=='Down sloping':
            self.slope_value.set('2')
        if self.defect_value.get()=='Normal':
                self.defect_value.set('1')
        elif self.defect_value.get()=='Fixed defect':
            self.defect_value.set('2')
        elif self.defect_value.get()=='Reversible defect':
            self.defect_value.set('3')
        try:
            self.patient_details=np.array([[int(self.age_value.get()),int(self.sex_value.get()),int(self.chest_value.get()),int(self.restingBP_value.get()),int(self.chol_value.get()),int(self.fastBS_value.get()),int(self.ecg_value.get()),int(self.heart_rate_value.get()),int(self.induced_cp_value.get()),float(self.peak_value.get()),int(self.slope_value.get()),int(self.ca_value.get()),int(self.defect_value.get())]])
            
            #data
            self.data=pd.read_csv('datasets/cleveland.csv')
            self.x=self.data.iloc[:,:-1].values
            self.y=self.data.iloc[:,-1].values
            #training
            self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.x,self.y,test_size=.2,random_state=40) 
            self.sc=StandardScaler()
            self.x_train=self.sc.fit_transform(self.x_train)
            self.x_test=self.sc.transform(self.x_test)
            self.patient_details=self.sc.transform(self.patient_details)
            #making predictions
            self.lr=SVC(C=10, gamma=0.01, random_state=0)

            self.lr.fit(self.x_train,self.y_train)
            self.y_pred=self.lr.predict(self.patient_details)
            self.name_2=self.name_value.get()
            self.p_id=self.id_num_value.get()
            self.clear()
            messagebox.showinfo('success','wait for result')
            
            speech=pyttsx3.init()
            voice=speech.getProperty('voices')
            speech.setProperty('rate',159)
            speech.setProperty('voice',voice[1].id)
            data={'Patient ID':[self.p_id] ,'Patient Name':[self.name_2] , 'Heart Condition':[self.y_pred[0]]}
            df=pd.DataFrame(data,columns=['Patient ID','Patient Name','Heart Condition'])
            df.to_csv('patient_records.csv',index=False,mode='a',header=False)
            
            
            for x in self.y_pred:
                if x==1:
                    speak=self.name_2 +', you likely have a heart disease. see a doctor please'
                    speech.say(speak)
                    speech.runAndWait()
                    self.result_label.config(text=self.name_2+', you likely have a heart disease. see a doctor please',fg='red')
                else:
                    speak=self.name_2+', congratulations, you do not have a heart disease, stay safe and take good care of your heart'
                    speech.say(speak)
                    speech.runAndWait()
                    self.result_label.config(text=self.name_2+', congrats, you do not have a heart disease, stay safe and take good care of your heart',fg='green')
            
            
        except Exception as e:
            self.clear()
            messagebox.showerror("ERROR ALERT",'please check details supplied,there is an error')
           
            
        
    def clear(self):
        self.id_num.delete(0,END)
        self.name.delete(0,END)
        self.age.delete(0,END)
        self.sex.set('choose sex')
        self.chest_value.set('yes not too severe')
        self.restingBP_val.delete(0,END)
        self.chol_val.delete(0,END)
        self.fastBS_val.set('Yes')
        self.ecg.set('Choose range')
        self.heart_rate.delete(0,END)
        self.induced_cp.set('yes')
        self.peak.delete(0,END)
        self.slope_val.set('Up sloping')
        self.ca_val.set('0')
        self.defect_val.set('Normal')
        
        

if __name__=="__main__":
	win=themed_tk.ThemedTk(theme='breeze')
	obj=Heart(win)
	win.mainloop()
