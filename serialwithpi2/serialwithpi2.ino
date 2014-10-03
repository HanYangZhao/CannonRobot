#include <AFMotor.h>

AF_DCMotor motor(3, MOTOR12_64KHZ); // create motor #2, 64KHz pwm
AF_DCMotor motor2(4, MOTOR12_64KHZ);
char serial_in;

void setup(){
  Serial.begin(9600);
  
  
 }
 
void loop(){ 
  if (Serial.available() > 0){
    serial_in = Serial.read();
    //going forward
    if( serial_in =='1'){
        motor.setSpeed(255); // set the speed to 200/255
        motor2.setSpeed(255);
        motor.run(FORWARD); 
        motor2.run(FORWARD);
    }
    //going backwards        
    else if( serial_in =='2'){
        motor.setSpeed(255); // set the speed to 200/255
        motor2.setSpeed(255);
        motor.run(BACKWARD); // turn it on going forward
        motor2.run(BACKWARD);
    }
    //turn left        
    else if( serial_in =='3'){
        motor.setSpeed(255); // set the speed to 200/255
        motor2.setSpeed(20);
        motor.run(FORWARD);
        motor2.run(FORWARD); 
        //motor2.run(BACKWARD);
    }
    //turn right   
    else if( serial_in =='4'){
       motor.setSpeed(20); // set the speed to 200/255
       motor2.setSpeed(255);
       motor.run(FORWARD);
        //motor.run(BACKWARD); // turn it on going forward
       motor2.run(FORWARD);
    }
    else {
      motor.run(RELEASE);
      motor2.run(RELEASE);
    }
  delay(10);
  }
}  
     
