def machineStart(){
    def status
    try{
        cscript = "cd jenkins;my_aws.py start"
        }        
    } catch (error) {
        throw error
    } finally {
        // junit '**/assertions.xml'
    }
    return status
}

