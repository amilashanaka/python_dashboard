# page1.py
import foo
foo.hello = 123

# page2.py
import foo
st.write(foo.hello)  # If page1 already executed, this should write 123