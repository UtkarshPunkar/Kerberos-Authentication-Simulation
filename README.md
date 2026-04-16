### 🪪 Kerberos Authentication Workflow Simulation.

This is a web-based simulation of the Kerberos authentication protocol. It is built with Python Flask, HTML, CSS, and JavaScript. The project shows how Kerberos works in a distributed system, covering client authentication to service access.

### 🧩 Features:

User Authentication Simulation  
It demonstrates how authentication happens with the Authentication Server (AS), Ticket Granting Server (TGS), and access to the Service Server.

### 🪜 Step-by-Step Workflow Display 
Each step of Kerberos, including TGT, Service Ticket, and Service Access, is clearly displayed for the user.

### 🔃 Loading Screen & Countdown  
A visual loading screen simulates a secure connection with a 10-second countdown before accessing the service.

### 🤖 Service Server Dashboard

Randomly generated "accessible files" with icons and file cards  
Responsive grid layout  
Hover animations for file cards  
Logout button at the top-right corner  
Modern, Futuristic UI  
Glowing effects and animations  
Responsive and visually appealing interface  
Futuristic color theme for a professional look  

### 🪧 Demo Credentials  
Username    Password  
alice       password123  
bob         mypassword  
utkarsh     test123  

These credentials are for demo purposes only.

### 📐 Installation & Setup

Clone the repository or download the files.

Install Python dependencies:  
pip install flask  

Run the application:  
python app.py  

Open your browser:  
http://127.0.0.1:5000  

Login using the demo credentials to see the simulation.

### ⚒️ How It Works

The client logs in, and the username and password are checked in the simulation.  
The Authentication Server (AS) issues a TGT (Ticket Granting Ticket).  
The Ticket Granting Server (TGS) issues a Service Ticket using the TGT.  
The Service Server verifies the service ticket and grants access.  
The loading screen shows an animation of a secure connection.  
The Service Dashboard displays random files the user can access.

### 📝 Notes

This is a simulation/demo.  
No real encryption or network communication is involved.  
Credentials are hardcoded for educational purposes.  
You can extend this project by adding:  
- Clickable files showing content  
- Animated arrows to visualize AS to TGS to Service  
- A real database for user accounts  

### 🙎‍♂️ Author
Utkarsh Punkar  

Thanks for reading
 
