Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "192.168.50.50"
  config.vm.provision "ansible", run: "always" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end
