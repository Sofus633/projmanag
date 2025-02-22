import sqlite3


class Project:
    def __init__(self,idd="None", name="unamed" ,subject="no subject" ,description="No description", time=0):
        self.name = name
        self.subject = subject
        self.description = description
        self.time = time 
    def __str__(self):
        return f"{self.name}, {self.time}, {self.subject} : {self.description}" 

def load_proj(proj):
    return Project(*get_proj("SELECT * FROM projects"))



def get_proj(request):     
    with sqlite3.connect("dttb.db") as conn:
        c = conn.cursor()
        c.execute(request)
    return c.fetchall() 

def start_session(proj):
    print(f"starting session on {proj}")
    project = load_proj(proj)

def get_proj_name():
    return get_proj("SELECT name FROM projects")




if __name__ == "__main__":

    projn = get_proj_name()
    print(load_proj(projn[0]))
     
