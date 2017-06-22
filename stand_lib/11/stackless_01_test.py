import stackless  

def show():
   print 'Stackless Python'  
  
st = stackless.tasklet(show)()
st.run()

st = stackless.tasklet(show)()
st.alive
   
st.kill()
st.alive
   
stackless.tasklet(show)()
stackless.tasklet(show)()   
stackless.run()




