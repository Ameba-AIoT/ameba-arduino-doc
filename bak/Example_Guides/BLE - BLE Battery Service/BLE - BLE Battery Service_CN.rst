材料准备

-  AmebaPro2 [AMB82 MINI] x 1

-  Android / iOS 智能手机

范例说明

BLE使用的是服务器--客户端模型。服务器我们感兴趣的数据，而客户端连接到服务器来读取数据。通常，蓝牙外围设备充当服务器，而蓝牙中心设备充当客户端。服务器可以包含许多服务，每个服务包含一组数据。客户端可以发送读取或写入数据的请求，还可以订阅通知，以便服务器可以向客户端发送数据更新。
=====================================================================================================================================================================================================================================================================================

在本示例中，我们在Ameba蓝牙堆栈上设置了一个简单的电池服务，然后使用智能手机来连接Ameba的BLE外设并读取电池数据。

具体的步骤如下：

请确保在您的手机上安装了以下蓝牙应用程序。这些应用程序将向您显示由Ameba发送的原始数据，并允许您与数据进行交互。

这里推荐的应用程序是nRF connect，可在下面的链接中找到:

-  Android :
   https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp

-  iOS : https://apps.apple.com/us/app/nrf-connect/id1054362403

LightBlue是另一种也可以使用的应用程序，但是它的特性比较少:

-  Android :
   https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer

-  iOS : https://apps.apple.com/us/app/lightblue/id557428110

打开Arduino的范例，"Files" -> "Examples" -> “AmebaBLE” ->
“BLEBatteryService”.

|image1|

上传代码并在上传完成后按下Ameba上的reset按钮。

在您的手机上，打开蓝牙app，扫描Ameba广播的蓝牙信号，会出现一个名为“AMEBA_BLE_DEV”的设备。

|image2|

连接到Ameba蓝牙设备，应该会出现可用服务的列表。单击battery服务展开，可以看到电池电量数据值。方框右边高亮的箭头用于读取数据和订阅通知。点击单个箭头读取电池电量值，90%的电量值就会显示出来。

|image3|

单击三重箭头订阅电池电量值的更新，电池值将自动开始更新。

|image4|

串行监视器将显示每秒钟电池电量的增加。当您单击其中一个箭头时，运行在Ameba上的程序将得到通知，并打印显示出所采取的操作。

|image5|

程式码说明

BLEService和 BLECharacteristic用于创建在蓝牙设备上运行的电池服务实例。

*BLE.*\ configadvert
()->setAdvType(GAP_ADTYPE_ADV_IND)用于将广告类型设置为允许连接的通用无定向广告。

setReadCallback()
和setCCCDCallback()用于注册将在读取电池电量数据或用户启用通知时调用的函数。

*BLE.*\ configserver(1) 用于告诉蓝牙堆栈有一个服务将会运行。

addService()将电池服务注册到蓝牙堆栈。

.. |image1| image:: ../../_static/Example_Guides/BLE_-_BLE_Battery_Service/BLE_-_BLE_Battery_Service_CN_images/image01.png
   :width: 2.34783in
   :height: 3.55268in
.. |image2| image:: ../../_static/Example_Guides/BLE_-_BLE_Battery_Service/BLE_-_BLE_Battery_Service_CN_images/image02.png
   :width: 2.52083in
   :height: 5.04532in
.. |image3| image:: ../../_static/Example_Guides/BLE_-_BLE_Battery_Service/BLE_-_BLE_Battery_Service_CN_images/image03.png
   :width: 2.66667in
   :height: 5.33719in
.. |image4| image:: ../../_static/Example_Guides/BLE_-_BLE_Battery_Service/BLE_-_BLE_Battery_Service_CN_images/image04.png
   :width: 2.20833in
   :height: 4.41987in
.. |image5| image:: ../../_static/Example_Guides/BLE_-_BLE_Battery_Service/BLE_-_BLE_Battery_Service_CN_images/image05.png
   :width: 4.2013in
   :height: 2.8589in
