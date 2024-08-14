Introduction to IFTTT

IFTTT, known as If This Then That, is a website and mobile app and free
web-based service to create the applets, or the chains of simple
conditional statements. The applet is triggered by changes that occur
within other web services such as Gmail, Facebook, Telegram, Instagram,
Pinterest, Line Notify etc.

Preparation

AmebaPro2 [ AMB82-MINI ] x 1

An account from https://ifttt.com/ , to access IFTTT service\*

\*Note: Upon log in, there are several cloud and online services that
are integrated with IFTTT platforms. Some IFTTT services may require
IFTTT Pro+, that is an online billing service.

Example

Generate Applet from IFTTT

In this example, we obtain an example of IFTTT Applet to send email to
specified recipient.

To run the example, HTTP POST feature of the Ameba is used to post a
simple webhook service that is received by IFTTT platform and in turn be
used to trigger a response (sending an email).

After logging in https://ifttt.com/, click Create from the top bar.

Click “Add” to add the trigger.

Choose Webhooks service as shown below. Alternatively, search the
service by typing into the search bar.

After that, the available triggers will appear. Choose “Receive a Web
request”.

Next, an Event Name is required to identify the trigger successfully. In
this example, set the Event name as “test_event”.

Next, click Add in Then That field to create the action service taken in
response to the last trigger.

Choose Email as the action service.

Click on Send me an email.

Under the template of Send me an Email, the contents of the email, such
as subject and body is editable. Click Create Action to complete the
action. Take note that Email service is offered to the email address
registered under IFTTT account.

Post the Trigger via Ameba

Once the Applet is ready in the IFTTT dashboard, the example program can
be flashed onto the Ameba board to post the HTTP request. Open the
example code in “File” -> “Examples” -> “AmebaHttp” ->
“HTTP_IFTTT_Post”.

In the example program, edit the following 3 items inside the code to
make the program work.

The WiFi credentials to connect to the Wi-Fi hotspot or access point of
desirable choice.

Under the Host name field, enter the host name of the IFTTT service
“maker.ifttt.com”.

Under the Path name field, enter the “Event name” and key field “kPath”:
“/trigger/Event name/with/key/Key Field”.

Event name: The event name should be the same as the one specified in
the IFTTT applet. In this example, the event name is “test_event”.

Key Field: Available under webhook service in individual IFTTT account.

To obtain a key from documentation tab of the Webhooks, find the webhook
service in the Explore tab.

On the Webhooks service page, click on the “Documentation” tab.

The key can be found in the documentation page. Also, information on how
HTTP request can be used.

Once the example is ready, Connect the Ameba board via USB cable. On the
Arduino IDE, compile the code and upload the code onto Ameba and press
the reset button. After the event has been successfully fired,
“Congratulations! You have fired the test_event event” can be seen on
the serial monitor and an email reminder for this event will be
delivered.

Thereafter an email is sent to recipient email account registered at
IFTTT Applet and an email will be received.

IFTTT Line Notify

Alternatively, an example to send a message with the LINE messaging app
on iPhone or Android using IFTTT Applet is available. It can be achieved
by modifying the “Then That” settings.

You may follow the same steps previously in “Generate Applet from IFTTT”
section to create a Webhooks service as the trigger. The Event Name
required to identify the trigger will remain as “test_event”. Next,
click the “Add” button in “Then That” field to create the action service
taken in response to the last trigger.

Choose Line as the action service.

Click on “Send message”.

Click on “Connect” and login to your Line Account.

Select LINE account, set the Recipient to “1-on-1 chat with LINE Notify”
which means the message triggered by IFTTT will directly send to your
chats. Next, input your desired message in the input box under
“Message”. For sending images, you can insert a link to your photo in
the input box under “Photo URL”.

On the Arduino IDE, compile the code and upload the code onto Ameba and
press the reset button. After the event has been successfully fired, you
will receive a message from “LINE Notify” on your Mobile devices or PC.

|image01.png| |image02.png| |image03.png| |image04.png| |image05.png|
|image06.png| |image07.png| |image08.jpeg| |image09.png| |image10.png|
|image11.png| |image12.png| |image13.png| |image14.png| |image15.png|
|image16.png| |image17.png| |image18.png| |image19.png| |image20.png|
|image21.png| |image22.png|

.. |image01.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image01.png
.. |image02.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image02.png
.. |image03.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image03.png
.. |image04.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image04.png
.. |image05.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image05.png
.. |image06.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image06.png
.. |image07.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image07.png
.. |image08.jpeg| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image08.jpeg
.. |image09.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image09.png
.. |image10.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image10.png
.. |image11.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image11.png
.. |image12.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image12.png
.. |image13.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image13.png
.. |image14.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image14.png
.. |image15.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image15.png
.. |image16.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image16.png
.. |image17.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image17.png
.. |image18.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image18.png
.. |image19.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image19.png
.. |image20.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image20.png
.. |image21.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image21.png
.. |image22.png| image:: ../../../_static/_Example_Guides/_HTTP%20-%20Use%20IFTTT%20for%20Web%20Service/image22.png
