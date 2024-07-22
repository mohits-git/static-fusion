# Static Fusion

Easily convert your markdown files into html files (static stite) with Static Fusion

This is a small project completely built with Python and no any external libraries.

### Run Project Locally:-

- In order to run locally on your machine first you need to have `python3` installed.
- Clone repository:
  ```
  git clone https://github.com/mohits-git/static-fusion.git
  ```
- navigate to the project folder `cd static-fusion`
- Add your markdown files in the `content` folder at the root of the project (I also have added the demo markdown files for testing purpose in `content` folder)
- Add any static files, example: css files, images, etc. to the `static` folder at the root of the project.
- In your terminal run:
  ```
    ./main.sh
  ```
- Now in you browser, you can see your static site live at:
  ```
  http://localhost:8888
  ```

> You can checkout the Generated HTML files and copied static files in the `/public` directory at the root of the project. And make changes as per your requirement or if there is any error.

### To Run Tests:-
Run at the root of the project: 
```
./test.sh
```

> **Note**:- I didn't add the support for inline nested markdown (eg. \* italic and \*\*bold\*\* \*). I might add this feature in future. If you want to contribute to the project feel free to open a pull request ^_^

### Demo:

https://github.com/user-attachments/assets/b522bdfb-10e4-4b26-b29e-8a0d7e44638f

