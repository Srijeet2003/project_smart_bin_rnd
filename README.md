# SKIDS: An Object Classification and Smart Communication based Waste Bin

This research paper aims to comprehensively discuss the
design, development, and evaluation of an ML-based Smart
Bin prototype. It will delve into the theoretical foundations of
ML algorithms, the hardware and software components of the
Smart Bin, the process of data collection and training, and the
performance evaluation of the prototype in real-world
scenarios.

## Description

The study introduces SKIDS, a Smart Bin system
using IoT for effective waste management. It utilizes YOLOv8 for
object detection and classification, integrating a custom dataset.
Firmata serves as a communication protocol between
microcontrollers and host computers, with PyFirmata enabling
Python interaction. Hardware includes a servo motor controlled
by PyFirmata for classification of Plastic and Non-Plastic Waste,
an ultrasonic sensor for distance measurement, and Arduino IDE
for control. The system employs the Bluetooth Terminator app to
alert garbage collection vehicles based on bin capacity. Integration
of communication modules, sensors, and machine learning
facilitates intelligent waste management and segregation.
Experimental evaluation demonstrates the system's ability to
accurately categorize waste types and improve collection
procedures compared to traditional methods. Performance metrics
such as accuracy, precision, and recall validate its effectiveness in
promoting sustainable urban environments through ML-based
waste management.

![Screenshot from 2025-06-16 23-27-20](https://github.com/user-attachments/assets/965f363d-51c7-4ca4-99b4-df7746070cbd)

## Getting Started

### Dependencies

* Ardruino IDE
* Ultralytics YOLOv8
* PyFirmara
* Bluetooth terminator app

## Future work

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
