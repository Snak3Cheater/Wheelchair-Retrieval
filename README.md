# Handicap Helper
Wheelchair Retrieval using Python, RPi, Tensorflow

1. Introduction/Background

Currently there are no automated or autonomous wheelchair retrieval products in the
consumer market. All currently available solutions require a significant amount of money and
material resources as well as the necessity of having a user be present during the entire retrieval
process. The Handicap Helper was designed to assist those with difficulty obtaining their own
wheelchair in a safe and hands-free way. There are many situations where the wheelchair would
be useful. When the wheelchair is out of reach the Handicap Helper can retrieve the wheelchair
and bring it back to the user. The wheelchair can also be too heavy to move or push for the user.
The Handicap Helper will also be able to pull the wheelchair for the user. The Handicap Helper
works best for people that are alone and unable to move the wheelchair. This project provides a
solution for those people and aims to help make it easier for retrieving their wheelchair.
The Handicap Helper solution aims to be cost effective for the user. We aim to cost less
than motorized wheelchairs and be built specifically for manual wheelchairs. This is due to
manual wheelchairs being the cheapest and adding on the Handicap Helper would add useful
functionalities for the user. With the cost in mind we made sure to build the Handicap Helper
using low cost and sturdy materials. We also used open source machine learning software which
makes implementation of autonomous features much easier. Using open source software also
allows us to utilize it as a tool for building robot autonomy with no additional costs for
prototyping. Putting it all together we ended up prototyping the wheelchair using less than $750.
This makes it cheaper than most of the modern wheelchairs but the wheelchairs in the market do
not have any built in autonomy. 

2. Project Breakdown

There are 3 main goals for this project. The robot must be able to:

    ● Find a specific object in a room, in this case the object will be a wheelchair.
  
    ● Once the wheelchair has been identified, the robot must go towards the object and attempt to move it.
  
    ● Finally, once the robot has acquired the object, it will need to bring that object to the user.
  
Breakdown of Goal #1:

To find the wheelchair, the robot needs to map the area it is in. The robot can do so
through the use of its ultrasonic sensors. The ultrasonic sensors will help the Handicap Helper
navigate through the room by avoiding obstacles and making its way back to the user. Through
the use of machine learning AI such as TensorFlow, we are able to provide the robot with the
ability to avoid obstacles and detect objects such as the wheelchair and distinguish between
predetermined markers such as hand gestures to make its way to the user's desired location.

Breakdown of Goal #2:

The 2nd goal assumes that the robot has spotted the wheelchair. The robot will approach
the wheelchair assuming there is nothing in the way. If there are objects in the way and the robot
has mapped the location of the wheelchair, we can use pathfinding algorithms to guide the robot
towards the chair. Once the Handicap Helper has positioned itself in front of the wheelchair, the
hooks on the chassis will retract outward and latch onto the metal framework of the chair itself.
The retractable hooks will fit on any standard sized wheelchair and can be modified for bigger or
smaller versions assuming that the dimensions are given beforehand. With this in mind, two
cases must be considered:

Case #1: The robot has the strength to move between 45-60 lbs (standard wheelchair weight)
○ With strong enough DC motors the robot will align itself from the bottom of the
wheelchair. Once centered in front of the wheelchair, the retractable hooks will 
activate and shoot outwards pulling the wheelchair towards the user while
avoiding obstacles.

Case #2: The robot does not have the strength to pull the chair

    ○ If the robot is unable to move the wheelchair itself, the strength of the gear motors must be increased to compensate for the weight increase. This will only occur if the wheelchair is outside of the specified target movement weight. Higher weighted wheelchairs could be moved if they were placed on smooth terrain, albeit at a much slower rate and with less precision. Once the robot has acquired the chair, it will have completed goal #2.

Breakdown of Goal #3:

The robot now has located and acquired the wheelchair. All that is left is to navigate the
wheelchair back to the user . This can be accomplished through manual control or autonomous
driving depending on where the wheelchair is located in the room and if the user can visually see
the chair. The object detection model we’ve created has been trained to distinguish between
certain markers to make wheelchair retrieval faster and more intuitive. In addition to labeling the
different sides of the wheelchair, the user's hand gestures will be used to signal the Handicap
Helper towards the deserted location of the user.

3. Schematics/Function Breakdown

Below is a rough schematic drawing of the robot which shows the main components that
will be used to path find and locate the wheelchair. That will be done using the front camera and
ultrasonic sensor. In the case of pulling the chair we will have retractable hooks that will come
out and hook on to the wheelchair pulling it through the best path.
The rough schematic below was done on LTSpice and is just a representation of how the
circuit will be connected to the Raspberry Pi. As you can see the camera will be connected via a
ribbon cable to the Raspberry Pi. The ultrasonic sensor we are using has its pin2 and pin5 as the
trig and echo. There are also 6 servo motors in the circuit and four of them will be used for the 
wheels while 2 of them will be used for the retractable hooks. Lastly we will have a 12V battery
power all major components in addition to the 5V supplied by the Raspberry Pi.

4. Major Parts

● CanaKit Raspberry Pi 8G Ram ($97.53)

    ○ https://www.amazon.com/gp/product/B08DJ9MLHV/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1

● Samsung Evo 64GB SD Card ($12.31)

    ○ https://www.amazon.com/gp/product/B08879MG33/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1

● UltraSonic Sensor MB1200 Max Sonar ($49.45)

    ○ https://www.maxbotix.com/ultrasonic_sensors/mb1200.htm

● MakerFocus DIY Robot Car ($17.99)

    ○ https://www.amazon.com/Makerfocus-80-260V-Multimeter-VoltmeterTransformer/dp/B01LYZDP9U/?_encoding=UTF8&pd_rd_w=7myqS&pf_rd_p=38316967-9a6c-4cf3-acd3-6269fd389669&pf_rd_r=GYPPBFKFYFZ9REKEYWAF&pd_rd_r=5d3b8e49-b826-400a-b436-587a5af171fa&pd_rd_wg=h6fkJ&ref_=pd_gw_ci_mcx_mr_hp_d

● BRINGSMART 12V 27rpm DC Worm Gear Motor ($119.96)

    ○ https://www.amazon.com/dp/B07F8Q73VC?ref=ppx_yo2_dt_b_product_details&th=1

● Plastic Wheels 6’’ x 1.5’’ ($43.22)

    ○ https://www.homedepot.com/p/Powercare-6-in-x-1-5-in-Universal-Plastic-Wheelfor-Lawn-Mowers-460435/100147219

● 8mm Flange Coupling Connector, Rigid Guide Steel Model Coupler Accessory, Shaft
Axis Fittings for DIY RC Model Motors, High Hardness Coupling Connector-Silver
($13.99)

    ○ https://www.amazon.com/gp/product/B07PFX4RDJ/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1

● TalentCell Rechargeable 12V 6000mAh/5V 12000mAh DC Output Lithium Ion Battery
Pack for LED Strip and CCTV Camera, Portable Li-ion Battery Bank with Charger,
Black ($37.99)

    ○ https://www.amazon.com/gp/product/B00ME3ZH7C/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1

● Power USB Switch Type-C Cable for Raspberry Pi 4 ($5.89)

    ○ https://www.amazon.com/gp/product/B07VLW8Q6T/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1

● Nulaxy C903 HD Webcam, 1080P Webcam with Microphone ($24.99)

    ○ https://www.amazon.com/gp/product/B08PBFYNF8/ref=ppx_yo_dt_b_asin_title_o08_s00?ie=UTF8&psc=1

● Construction Materials ($300)
Totaling: $723.32

5. Code Design/Breakdown
The basic functionality of the Handicap Helper can be broken down into four different sections:
● Camera based object detection
● Autonomous driving and object avoidance using ultrasonic sensors
● Manual movement using high torque DC gear motors
● Wheelchair retrieval using and custom hook and servo motor combo
All components will be fed into our microcontroller and Raspberry Pi in addition to the user
giving their own input using our custom GUI. The GUI will allow the user to enable different
functions and give the user feedback on the robot’s current status.
The robot can be set to different settings which can be toggled by the user. The functions are
located on the GUI and can be clicked to enable or disable the function. Each of the functions
have the following features:
Manual Mode
In manual mode the user can take control of the robot directly. The robot can be
controlled with the following buttons on the GUI. The WASD keys control the movement of the
robot such as going forward, reversing and turning. The ZX keys control the function of the
retractable hooks where you can retract or clamp the hooks. Combining these the user can drive
the robot around and use the clamping buttons to get the chair manually and bring it back.
Search Mode and Search Person
In Search Mode the robot will actively look for the wheelchair using the front mounted
camera. The object detection software will be running and will determine which side of the
wheelchair the robot is facing. From there the robot will try to position itself towards the front of
the wheelchair and center itself in which it will print to the console whether the wheelchair is
centered on the camera or not.
Search Person mode operates under the same principles of the search mode except now
the robot is looking for a hand gesture from the person. Once a hand gesture is found on the
camera the robot will go towards it.
Explore Mode
In explore mode the robot will just randomly wander around its location until other
functions are activated. The robot will actively explore and avoid obstacles along the way.

6. Chassis Design
The Handicap Helper was designed to be sized universally for all wheelchairs (between
45-60lb). The main body of the chassis, the retractable hooks, and the main support beams are all
made from aluminum. Aluminum is a cheap and light material and has the strength to withstand
the force that will be applied to the robot. We used aluminum as the frame for the robot to 
provide stability and support from the base. More importantly, we used aluminum on the sides
and built up a tower to house the servo motors for the retractable hooks. The side housing the
retractable hooks needed the aluminum as the servo motors could over-retract or under-retract in
which the hooks would hit the tower. With aluminum, the hooks could hit the tower will no
damage as well as solve the over retracting or under retracting by stopping the servo motors.
Our electrical components like the Raspberry Pi, external power source, and drive control
PCB will all be mounted on a wooden base placed on top of the robot. The base of the robot is
wood as wood is a cheap material. The wood also provides more weight to the robot so that the
robot won’t tip or fall over when attempting to pull a wheelchair. Given that wheelchairs are
around 45lb to 60lbs, the robot needs weight to keep it on the ground when pulling the chair.
Wood became a cheap and alternative solution to other weighted materials as we did not want to
make the robot too heavy with metals. The circuitry will sit on top of the wooden base where it
can be glued and held in place. The bottom diagrams show the different sides of the robot. From
left to right the views are the top view, side view and front view.
7. Pics of robot

9. Conclusions
Although there are smart automatic wheelchairs, there are none that can be called to the
user when the user is away from the chair. We seek to create a solution for the user to be able to
call the wheelchair to themselves both manually and automatically. The bot we are making is
separate from the chair. The cost of the bot will be significantly less than these smart automatic
wheelchairs costing below $1,000. The bot will work with manual wheelchairs and will bring the
chair to the user. If the user leaves their chair somewhere around the house the bot should be able
to find and retrieve the chair. This is a better solution for people that can’t afford to buy an 
automatic chair or for people that already have a manual wheelchair and just need the
functionality of calling their chair to themselves.

9. Future Improvements
In terms of future improvements we would like to have upgraded to stronger gear motors
to improve on retrieval speed and accuracy. We would also like to use a better camera
preferably one that would rotate in order to improve on object detection and require less turning.
Another improvement would be to increase the object detection accuracy by supplying an
algorithm that included various lighting conditions and camera angles of the hand gestures and
wheelchair to build on machine learning. Next is to develop a SLAM algorithm and self
mapping function for better efficiency using components such as a LiDAR. Lastly having finer
movement controls that would allow for better obstacle avoidance and precise turns such
creating a chassis that would not require that wide of turns.

10. References
Ultrasonic Sensor MB1200 Max Sonar DataSheet
• https://www.maxbotix.com/documents/XL-MaxSonar-EZ_Datasheet.pdf
Raspberry Pi 4 Model B 8Gb
• https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2711/rpi_D
ATA_2711_1p0_preliminary.pdf
Servo Motor MG996R
• https://components101.com/asset/sites/default/files/component_datasheet/MG996
R-Datasheet.pdf
Tensor Flow Object Detection Software
• https://www.tensorflow.org/lite/examples/object_detection/overview
