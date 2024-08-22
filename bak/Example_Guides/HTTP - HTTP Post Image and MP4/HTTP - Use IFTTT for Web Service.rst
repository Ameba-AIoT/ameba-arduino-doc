Introduction to IFTTT
=====================

IFTTT, known as If This Then That, is a website and mobile app and free
web-based service to create the applets, or the chains of simple
conditional statements. The applet is triggered by changes that occur
within other web services such as Gmail, Facebook, Telegram, Instagram,
Pinterest, Line Notify etc.

Preparation
===========

-  AmebaPro2
   [ `AMB82-MINI <https://www.amebaiot.com/en/amebapro2/#rtk_amb82_mini>`__ ]
   x 1

-  An account from https://ifttt.com/ , to access IFTTT service\*

|1|

\*Note: Upon log in, there are several cloud and online services that
are integrated with IFTTT platforms. Some IFTTT services may require
IFTTT Pro+, that is an online billing service.

Example
=======

-  Generate Applet from IFTTT

In this example, we obtain an example of IFTTT Applet to send email to
specified recipient.

To run the example, HTTP POST feature of the Ameba is used to post a
simple webhook service that is received by IFTTT platform and in turn be
used to trigger a response (sending an email).

After logging in https://ifttt.com/, click **Create** from the top bar.

|image1|

Click “Add” to add the trigger.

|image2|

Choose Webhooks service as shown below. Alternatively, search the
service by typing into the search bar.

|image3|

After that, the available triggers will appear. Choose “Receive a Web
request”.

|A picture containing text Description automatically generated|

Next, an Event Name is required to identify the trigger successfully. In
this example, set the Event name as “test_event”.

|image4|

Next, click Add in Then That field to create the action service taken in
response to the last trigger.

|image5|

Choose Email as the action service.

|image6|

Click on Send me an email.

|Graphical user interface Description automatically generated|

Under the template of Send me an Email, the contents of the email, such
as subject and body is editable. Click Create Action to complete the
action. Take note that Email service is offered to the email address
registered under IFTTT account.

|image7|

-  Post the Trigger via Ameba

| Once the Applet is ready in the IFTTT dashboard, the example program
  can be flashed onto the Ameba board to post the HTTP request.
| Open the example code in “File” -> “Examples” -> “AmebaHttp” ->
  “HTTP_IFTTT_Post”. |Graphical user interface Description automatically
  generated with low confidence|

In the example program, edit the following 3 items inside the code to
make the program work.

1. The WiFi credentials to connect to the Wi-Fi hotspot or access point
   of desirable choice.

2. Under the Host name field, enter the host name of the IFTTT service
   “maker.ifttt.com”.

3. Under the Path name field, enter the “Event name” and key field
   “kPath”: “/trigger/Event name/with/key/Key Field”.

-  Event name: The event name should be the same as the one specified in
   the IFTTT applet. In this example, the event name is “test_event”.

-  Key Field: Available under webhook service in individual IFTTT
   account.

|Graphical user interface, text, application Description automatically
generated|

To obtain a key from documentation tab of the Webhooks, find the webhook
service in the Explore tab.

|image8|

On the Webhooks service page, click on the “Documentation” tab.

|image9|

The key can be found in the documentation page. Also, information on how
HTTP request can be used.

|image10|

| Once the example is ready, Connect the Ameba board via USB cable.
| On the Arduino IDE, compile the code and upload the code onto Ameba
  and press the reset button. After the event has been successfully
  fired, “Congratulations! You have fired the test_event event” can be
  seen on the serial monitor and an email reminder for this event will
  be delivered.

|image11|

Thereafter an email is sent to recipient email account registered at
IFTTT Applet and an email will be received.

|image12|

-  IFTTT Line Notify

Alternatively, an example to send a message with the LINE messaging app
on iPhone or Android using IFTTT Applet is available. It can be achieved
by modifying the “Then That” settings.

You may follow the same steps previously in “Generate Applet from IFTTT”
section to create a Webhooks service as the trigger. The Event Name
required to identify the trigger will remain as “test_event”. Next,
click the “Add” button in “Then That” field to create the action service
taken in response to the last trigger.

|image13|

Choose Line as the action service.

|Graphical user interface, application Description automatically
generated|

Click on “Send message”.

|image14|

Click on “Connect” and login to your Line Account.

|image15|

Select LINE account, set the Recipient to “1-on-1 chat with LINE Notify”
which means the message triggered by IFTTT will directly send to your
chats. Next, input your desired message in the input box under
“Message”. For sending images, you can insert a link to your photo in
the input box under “Photo URL”.

|image16|

On the Arduino IDE, compile the code and upload the code onto Ameba and
press the reset button. After the event has been successfully fired, you
will receive a message from “LINE Notify” on your Mobile devices or PC.

|A screenshot of a video game Description automatically generated with
medium confidence|

.. |1| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image01.png
   :width: 6.27in
   :height: 3.40669in
.. |image1| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image02.png
   :width: 6.27in
   :height: 0.91068in
.. |image2| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image03.png
   :width: 6.27in
   :height: 4.98766in
.. |image3| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image04.png
   :width: 6.26806in
   :height: 3.42194in
.. |A picture containing text Description automatically generated| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image05.png
   :width: 6.26806in
   :height: 5.20486in
.. |image4| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image06.png
   :width: 6.26806in
   :height: 5.01181in
.. |image5| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image07.png
   :width: 6.26806in
   :height: 4.84167in
.. |image6| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image08.png
   :width: 6.26806in
   :height: 3.77014in
.. |Graphical user interface Description automatically generated| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image09.png
   :width: 6.26806in
   :height: 4.39236in
.. |image7| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image10.png
   :width: 6.26806in
   :height: 5.75069in
.. |Graphical user interface Description automatically generated with low confidence| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image11.png
   :width: 6.26806in
   :height: 6.98472in
.. |Graphical user interface, text, application Description automatically generated| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image12.png
   :width: 6.26806in
   :height: 6.96042in
.. |image8| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image13.png
   :width: 6.26806in
   :height: 2.83194in
.. |image9| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image14.png
   :width: 6.26806in
   :height: 3.2375in
.. |image10| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image15.png
   :width: 6.26806in
   :height: 2.88056in
.. |image11| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image16.png
   :width: 6.26806in
   :height: 6.14444in
.. |image12| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image17.png
   :width: 6.22909in
   :height: 5.34687in
.. |image13| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image07.png
   :width: 6.26806in
   :height: 4.84167in
.. |Graphical user interface, application Description automatically generated| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image18.png
   :width: 6.27784in
   :height: 3.71591in
.. |image14| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image19.png
   :width: 6.26806in
   :height: 4.41389in
.. |image15| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image20.png
   :width: 4.87106in
   :height: 4.69566in
.. |image16| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image21.png
   :width: 6.26806in
   :height: 6.79306in
.. |A screenshot of a video game Description automatically generated with medium confidence| image:: ../../_static/Example_Guides/HTTP_-_Use_IFTTT_for_Web_Service/HTTP_-_Use_IFTTT_for_Web_Service_images/image22.jpeg
   :width: 4.05172in
   :height: 8.01724in
