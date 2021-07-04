## this code will run in Jupyter Notebook 
## start Jupyter from Anaconda in Start menu.
# coding: utf-8

# In[1]:


import swat


# In[2]:


s = swat.CAS("server", 8777, "student", "Metadata0", protocol="http")


# In[4]:


s.table.addCaslib(
  name="customer data",
  description="customer data",
  dataSource={"srctype":"path"},
  path="/workshop/didp/data/sas_data/customer_data")


# In[5]:


s.table.fileInfo(path="%customers%",kBytes=True)


# In[6]:


s.table.columnInfo(table="customers.sas7bdat")


# In[7]:


result = s.table.loadTable(path="customers.sas7bdat",casout={"name":"cust","replace":True})
cust = s.CASTable(result.tableName)
                                                              
cust=s.CASTable("customers.sas7bdat")
s.table.fetch(
table="cust",
format=True,
to=5,
sortBy=[
    {"name":"Customer_City", "order":"descending"}
      ]
)


# In[8]:


s.table.save(table="customers.sas7bdat", name="customer_copy.sashdat",replace=True)
s.table.fileInfo(path="customer_copy.sashdat")


# In[13]:


s.dataStep.runCode(
code='''
data "customers_stnd";
    length "CUSTOMER_STATE_STND"n varchar(256);                                                  
    set "cust" ;
    "CUSTOMER_STATE_STND"n = dqstandardize ("CUSTOMER_STATE"n, "State/Province (Full Name)", "ENUSA");
    
run;''')


# In[15]:


s.table.fetch(
table = "customers_stnd",
    sortBy = [
        {"name":"customer_state_stnd"}
    ]
)

