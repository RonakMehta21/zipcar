# **Team FourReal**
Project for implementing ZipCar.net, a Car rental site designed for millennial fast life!

Application Demo: https://zipcarlive.herokuapp.com/

## **Group Members:**

* Nupur Yadav
* Chetan Kulkarni
* Lokesh Vadlamudi
* Ronak Mehta

## **[Project Board](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/projects/1)**

## **[Project Journal](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/tree/master/Documents/Journal)**

## **[Google Sprint Task Sheet](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Documents/Sprint%20Task%20Sheet_Four%20Real.xlsx)**

## **Burn Down Chart:**


![Image description](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Images/FourRealBurnDownChart.png)

## **XP Core Values Implemented:**

* Nupur Yadav - [Communication](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Documents/XP_CoreValues.md)
* Chetan Kulkarni - [Simplicity](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Documents/XP_CoreValues.md)
* Lokesh Vadlamudi - [Courage](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Documents/XP_CoreValues.md)
* Ronak Mehta - [Feedback](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Documents/XP_CoreValues.md)

## **Architecture Diagram:**

![Image description](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Images/Architecture%20Diagram.jpeg)

## **Component Diagram:**

![Image description](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Images/Component%20Diagram.jpeg)

## **Deployment Diagram:**

![Image description](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Images/Deployment%20Diagram.jpeg)

## **Design Pattern:**
We have used Django's MTV (Model, Template and View) architecture which is a slight variation of MVC architecture as shown below.

![Image description](https://miro.medium.com/max/1400/0*8ZFh-CsrMi7bQG0O.jpg)

Photo Credit : https://miro.medium.com/max/1400/0*8ZFh-CsrMi7bQG0O.jpg

**Working of MTV architecture:**

![Image description](https://miro.medium.com/max/1400/0*r7ALulxaXPSboehX.jpg)

Photo credit : https://miro.medium.com/max/1400/0*r7ALulxaXPSboehX.jpg

## Jmeter Stress Testing

Following screenshots shows the CPU utilization and network in/out when we hit our application with 1000 requests. It can be seen because of loadbalancing the traffic is divided among all the instances and a spike is seen in CPU utilization of all the instances.

**Instance 1**
![Image description](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Images/StressTesting_CPU_utilization.png)

**Instance 2**
![Image description](https://github.com/gopinathsjsu/sp20-cmpe-202-sec-49-team-project-fourreal/blob/master/Images/StressTesting_CPU%20utilization2.png)


