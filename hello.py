   pipeline {
     agent any
     stages {
       stage('Hello') {
         steps {
           echo 'Hello from Jenkins'
         }
       }
       stage('Run Python') {
         steps {
           sh 'python3 hello.py'
         }
       }
     }
   }
