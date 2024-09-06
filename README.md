### Installation

1. Install Node.js: Need to use v16.x, install via [NVM](https://github.com/nvm-sh/nvm)
2. Install Java(openjdk@11 ) 
    1. `brew install openjdk@11`
3. Download Android studio
    1. Install SDK, select your preferred version
    2. Go to SDK Tools uncheck “Hide Obsolete Packages”
    3. Install `Android SDK Command-line Tools`(adb) and `Android SDK Tools(obsokete)` 
4. [Install Appium Server](https://appium.io/docs/en/2.1/quickstart/install/)
    - `npm i --location=global appium`
    - [Appium extension CLI](https://appium.io/docs/en/2.1/cli/extensions/)
5. Install [UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver) (for Android)
    - `appium driver install uiautomator2`
6. Install Appium-Doctor
    - `npm install appium-doctor -g`
    - run`appium-doctor`

7. Install Dependencies
  - `pip install -r requirements.txt` 

### Run Test
1. Launch Appium Server `appium` default 4723
2. Run 
   ```
   python test_SmartBanking.py
   python test_Techcombank.py
   python test_VCB.py
   ```
