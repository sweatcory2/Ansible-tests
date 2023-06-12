# Final Project Automagic

This is where the magic doesn't happen, but rather is explained.

## List of requirements

- For testing purposes
    - spin up my own version of nautobot to have an inventory
    - spin up an eve instance to have "devices" to test on
    - create an inventory
    - have a central point to pull firmware from. 
    - at a minimum, get the firmware onto the devices that exist for a proof of concept.
    - create Ansible playbooks that will cause the pull to happen, and possibly install the firmware automatically.

## End State

- Replicate enterprise standards to the point that when implemented on Exped kits or enterprise devices, the automation piece works seamlessly.

## Topics of research

- Creating a Nautobot inventory that an API can call to.
- Learning NQE's on fwd-networks, for the purpose of having it integrate with Ansible.


```
cd existing_repo
git remote add origin http://10.10.44.20/Stud1/final-project-automagic.git
git branch -M main
git push -uf origin main
```

