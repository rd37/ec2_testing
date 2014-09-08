'''
Created on Sep 5, 2014

@author: ronaldjosephdesmarais
'''
import boto.ec2,threading,time

class ec2_instance(threading.Thread):
    conn=""
    region=""
    ami_id=""
    ec2_res=""
    ec2_inst=""
    ec2_inst_status=""
    
    def __init__(self,region,ami_id):
        threading.Thread.__init__(self)
        self.region=region
        self.ami_id=ami_id
        
    def run(self):
        self.init()
        self.boot_vm()
        
        while True:
            ec2_inst_status=self.conn.get_all_instance_status()
            for inst_state in ec2_inst_status:
                if self.ec2_inst[0].id == inst_state.id:
                    self.ec2_inst_status = inst_state
            
            if self.ec2_inst_status != "":
                if self.ec2_inst_status.system_status.details['reachability'] == 'passed':
                    break
            time.sleep(10)
       
        print "terminating instance"
        self.conn.terminate_instances(instance_ids=[self.ec2_inst[0].id])
            
    def init(self):
        print "initializing boto"
        self.conn = boto.ec2.connect_to_region(self.region)
    
    
    def boot_vm(self):
        print "booting ec2 vm"
        self.ec2_res=self.conn.run_instances(self.ami_id,key_name='idev-ec2-key',instance_type='t1.micro',security_groups=['idev-security-group'])
        self.ec2_inst=self.ec2_res.instances
        print "got back res %s with inst %s"%(self.ec2_res,self.ec2_inst)
    
if __name__ == '__main__':
   
    for i in range(1,10):
        inst = ec2_instance('us-west-2','ami-d9fabce9')
        inst.start()
        time.sleep(1)
    print "done"