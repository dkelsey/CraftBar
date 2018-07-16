# -*- mode: ruby -*-
# vi: set ft=ruby :

boxes = [
    {
        :box => "ubuntu/xenial64",
        :name => "ansible",
        :eth1 => "192.168.101.10",
        :mem => "1024",
        :cpu => "1",
        :gui => false,
        :additional_pkgs => [],
        :additional_scripts => [],
        :ports => [],
        :pip_pkgs => [],
        :pip_pkgs2 => []
    },
    {
        :box => "ubuntu/xenial64",
        :name => "craftbar",
        :eth1 => "192.168.101.11",
        :mem => "2048",
        :cpu => "1",
        :gui => false,
        :additional_pkgs => [ "libssl-dev", "libffi-dev" ],
        :additional_scripts => [ "/vagrant/provision_craftbar.sh" ],
        :ports => [ 5000, 8983 ],
        :pip_pkgs => [ "ansible", "psychopg2"],
        :pip_pkgs2 => [ "Django" ]
    },
    {
        :box => "ubuntu/xenial64",
        :name => "postgres",
        :eth1 => "192.168.101.12",
        :mem => "2048",
        :cpu => "1",
        :gui => false,
        :additional_pkgs => [ "postgresql" ],
        :additional_scripts => [ "/vagrant/provision_db.sh" ],
        :ports => [ 5432 ],
        :pip_pkgs => [ "ansible" ],
        :pip_pkgs2 => []
    }
]
=begin
    {
        :box => "ubuntu/xenial64",
        :name => "elk",
        :eth1 => "192.168.101.13",
        :mem => "2048",
        :cpu => "1",
        :gui => false,
        :additional_pkgs => [],
        :additional_scripts => [],
        :ports => [5601,9201],
        :pip_pkgs => [ "ansible" ],
        :pip_pkgs => []
    }
]
=end

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  boxes.each do |opts|
    config.vm.define opts[:name] do |config|
        config.vm.box = opts[:box]
        config.vm.hostname = opts[:name]
        config.vm.network "private_network", ip: opts[:eth1]

        if opts[:ports].any?
            opts[:ports].each do |port|
              config.vm.network "forwarded_port", guest: port, host: port
            
            # config.vm.network "forwarded_port", guest: opts[:ports][0], host: opts[:ports][0]
            end
        end

        config.vm.provider "virtualbox" do |vb|
            vb.customize ["modifyvm", :id, "--memory", opts[:mem]]
            vb.gui = opts[:gui]
        end

        # install python and pip
        config.vm.provision "shell", inline: <<-SHELL
            sudo apt-get update
            sudo apt-get -y upgrade

            sudo apt-get -y install libssl-dev
            # install python 3.x and pip
            sudo apt-get install -y python3
            sudo apt-get install -y python3-pip

            # this fixes an issue installing Django 
            sudo apt-get install -y python3.5-dev
            sudo -H pip3 install cryptography==1.5
            sudo -H pip3 install --upgrade pip
            sudo pip3 install ipython
        SHELL

=begin
        # install java
        config.vm.provision "shell", inline: <<-SHELL
    #<<COMMENT
            # # install java
            # sudo add-apt-repository ppa:webupd8team/java
            # sudo apt-get update
            #
            # echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
            # echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections
            # apt-get install --yes oracle-java8-installer
            # yes "" | apt-get -f install
    #COMMENT
=end


        if opts[:additional_pkgs].any?
            # install additional packages
            opts[:additional_pkgs].each do |pkg|
                config.vm.provision "shell" do |s|
                    s.inline = "sudo apt-get install $1 -y"
                    s.args = pkg
                end
            end
        end

        if opts[:additional_scripts].any?
            # install additional scripts to run
            opts[:additional_scripts].each do |script|
                config.vm.provision "shell" do |s|
                    s.inline = "sudo su -c $1 "
                    s.args = script
                end
            end
        end

#=begin
        if opts[:pip_pkgs2].any?
            # install pip packages with sudo -H
            config.vm.provision "shell" do |s|
                s.inline = "sudo -H pip install $1"
                s.args = opts[:pip_pkgs]
            end
        end
#=end


        if opts[:pip_pkgs].any?
            # install pip packages
            config.vm.provision "shell" do |s|
                s.inline = "pip3 install $1"
                s.args = opts[:pip_pkgs]
            end
        end


        config.vm.provision "file", source: "ansible_rsa", destination: "/home/ubuntu/.ssh/id_rsa"
        public_key = File.read("ansible_rsa.pub")
        config.vm.provision :shell, :inline =>"
            echo 'Copying ansible-vm public SSH Keys to the VM'
            mkdir -p /home/ubuntu/.ssh
            chmod 700 /home/ubuntu/.ssh
            echo '#{public_key}' >> /home/ubuntu/.ssh/authorized_keys
            chmod -R 600 /home/ubuntu/.ssh/authorized_keys
            echo 'Host 192.168.*.*' >> /home/ubuntu/.ssh/config
            echo 'StrictHostKeyChecking no' >> /home/ubuntu/.ssh/config
            echo 'UserKnownHostsFile /dev/null' >> /home/ubuntu/.ssh/config
            chmod -R 600 /home/ubuntu/.ssh/config
            ", privileged: false

    end

  end

end
