import java.awt.event.*; 
import javax.swing.*;
import java.awt.*;


class haha implements ActionListener{
JFrame frame;  
       Container contentPanel;  
       TextField tf1,tf2; 
       Label lab1,lab2;  
public haha(){  
    frame=new JFrame("Change Fahrenheit into Celsius! ");  
    contentPanel=frame.getContentPane();  
    contentPanel.setLayout(new FlowLayout());  
    lab1=new Label("Fahrenheit degree is ");  
    tf1=new TextField(10);  
    tf2=new TextField(10);  
    lab2=new Label("Celsius degree is "); 
    contentPanel.add(lab1);   
    contentPanel.add(tf1);   
    contentPanel.add(lab2); 
    contentPanel.add(tf2);  
    tf1.addActionListener(this);   
    frame.setSize(200,300);  
    frame.setVisible(true); }        
    public void actionPerformed(ActionEvent e){  
    if(e.getSource()==tf1){ 
    float n1=Float.parseFloat(tf1.getText());  // Enter 32
    float n2=(float)(5.0/9.0*(n1-32));  
    tf2.setText(""+n2); } }
    public static void main(String args[]){
        new haha();
    }
} 