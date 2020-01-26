# Setting up Nexus 9000v using Vagrant

## Nexus 9000v Vagrant Box

At Cisco Live, you need to validate the image is downloaded and
reegistered with Vagrant.  The command to do this is:

```bash
vagrant box list
```

The output to expect is:

```bash
nxos/9.3.3    (virtualbox, 0)
```

If it's missing (shouldn't be missing, but they are public laptops),
the image itself can be found at **${HOME}/IOS/nexus9300v.9.3.3.box**

If you are working this module outside of Cisco Live, you'll need to
download **nexus9300v-9.3.3.box** from cisco.com.

To register the image with Vagrant, the command is:

```bash
vagrant box add nexus9300v/9.3.3 nexus9300v.9.3.3.box
```

Once registered, from this modules directly - specifically, with the
included Vagrantfile in the current directory - start the Vagrant box
image:

```bash
vagrant up
```

## Configure the NXOSv image for NXAPI and boot variable

```bash
bash -x enable_nxapi.sh
```

## For this workshop, you need to enable icam

```bash
python3 setup_nxos.py
```

## Cautions

Please note that you will get an error about session timing
out or /vagrant sync not working.  This is okay for the purposes of
this lab.

Please also note that the image could take 5-10 minutes to load.
