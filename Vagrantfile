# -*- mode: ruby -*-
# vi: set ft=ruby :

GUEST_USER = "vagrant"

boxes = [
    {
        :box => "ubuntu/xenial64",
        :name => "jenkins",
        :eth1 => "192.168.101.10",
        :mem => "1024",
        :cpu => "1",
        :gui => false,
        :additional_pkgs => [],
        :additional_scripts => ["/vagrant/provision_jenkins.sh"],
        :ports => [ 8080 ],
        :pip_pkgs => []
    },
    {
        :box => "ubuntu/xenial64",
        :name => "craftbar",
        :eth1 => "192.168.101.11",
        :mem => "2048",
        :cpu => "1",
        :gui => false,
        :additional_pkgs => [ "libssl-dev", "libffi-dev", "python3-psycopg2", "sqlite" ],
        :additional_scripts => [ "/vagrant/provision_craftbar.sh" ],
        :ports => [ 5000, 8983 ],
        :pip_pkgs => []
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
        :pip_pkgs => []
    }
]

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  boxes.each do |opts|
    config.vm.define opts[:name] do |config|
        config.vm.box = opts[:box]
        config.vm.hostname = opts[:name]
        config.vm.network "private_network", ip: opts[:eth1]

          config.vm.synced_folder "CraftBar/CraftBar/", "/home/#{GUEST_USER}/CraftBar"

          if opts[:ports].any?
              opts[:ports].each do |port|
                config.vm.network "forwarded_port", guest: port, host: port
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
                      s.inline = "chmod u+x $1 && sudo su -c $1 "
                      s.args = script
                  end
              end
          end

          if opts[:pip_pkgs].any?
              # install pip packages
              config.vm.provision "shell" do |s|
                  s.inline = "pip3 install $1"
                  s.args = opts[:pip_pkgs]
              end
          end


          config.vm.provision "file", source: "ansible_rsa", destination: "/home/#{GUEST_USER}/.ssh/id_rsa"
          public_key = File.read("ansible_rsa.pub")
          config.vm.provision :shell, :inline =>"
              echo 'Copying ansible-vm public SSH Keys to the VM'
              mkdir -p /home/#{GUEST_USER}/.ssh
              chmod 700 /home/#{GUEST_USER}/.ssh
              echo '#{public_key}' >> /home/#{GUEST_USER}/.ssh/authorized_keys
              chmod -R 600 /home/#{GUEST_USER}/.ssh/authorized_keys
              echo 'Host 192.168.*.*' >> /home/#{GUEST_USER}/.ssh/config
              echo 'StrictHostKeyChecking no' >> /home/#{GUEST_USER}/.ssh/config
              echo 'UserKnownHostsFile /dev/null' >> /home/#{GUEST_USER}/.ssh/config
              chmod -R 600 /home/#{GUEST_USER}/.ssh/config
              ", privileged: false

    end

  end

end
