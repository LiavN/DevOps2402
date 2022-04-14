properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("one"){
        git "https://github.com/LiavN/DevOps2402.git"
    }   
    stage("bla"){
        sh "ls -l"
    }
}
