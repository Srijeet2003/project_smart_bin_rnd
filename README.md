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

## Conclusion

The future of IoT-based smart dustbins entails advancements
in AI and ML algorithms for predicting waste generation,
optimizing collections, and improving sorting accuracy. Our
system was able to detect plastic and non-plastic fairly with
good accuracy. The Bluetooth module along with the LCD
was used to indicate the live status of the smart bin. Financial
constraints, connectivity issues, and privacy concerns may
hinder adoption, necessitating energy-efficient tech and edge
computing. Overcoming prototype challenges like data
inconsistency and mechanical issues is vital. Addressing
obstacles like cost, connectivity, and privacy is crucial.
Innovative solutions such as energy-efficient tech and edge
computing are necessary for effective smart dustbin operation
in diverse urban environments, ensuring improved waste
management.

## Authors

Contributors names and contact info

- Shriya Chowdhury
- Soumo Roy
- Dishanwita Ghosh Chowdhury
- Srijeet Chakraborty
- Khyati Priya Jain
- Budhaditya Bhattacharyya

## Citation

```
@inproceedings{chowdhury2024skids,
  title={SKIDS: An Object Classification and Smart Communication based Waste Bin},
  author={Chowdhury, Shriya and Roy, Soumo and Chowdhury, Dishanwita Ghosh and Chakraborty, Srijeet and Jain, Khyati Priya and Bhattacharyya, Budhaditya},
  booktitle={2024 3rd International Conference on Artificial Intelligence For Internet of Things (AIIoT)},
  pages={1--6},
  year={2024},
  organization={IEEE}
}
```

## Acknowledgments

We would like to thank our professor Dr. Buddhaditya
Bhattacharya for his support, guidance and valuable time.
