# 1.1 Compare and contrast various types of security controls 
## **Made to supplement recent video that covers the 1.1 practice quiz**

**Categories**

* **Category Explained:** Categories define the *means* of implementation. When looking at a control, ask yourself: "Is this a computer script, a written rule, a human action, or a physical barrier?"  
  * **Technical:** Often called logical controls. These are implemented by systems, hardware, or software to restrict access or offer protection. Examples include Firewalls, Antivirus, Encryption, and Access Control Lists (ACLs).  
  * **Managerial:** Often called administrative controls. These are the "paperwork" and oversight of security. They focus on risk management \[managing risk\] and policy creation. Examples include Risk Assessments, Security Policies, Standard Operating Procedures (SOPs), Security Awareness Training, Organizational security policy.  
  * **Operational:** These are the "people" controls. They represent the day-to-day actions performed by humans to support the security goals. Examples include Security Guards, Awareness Training, Incident Response teams, Configuration Management  
  * **Physical:** Controls you can touch that prevent physical access to assets. Examples include Fences, Locks, Bollards, and Lighting.  
* **How it connects to related concepts:** This connects directly to **Security Governance (5.1)**. Managerial controls (like policies) are created by governance bodies, which then dictate the Technical controls (like firewalls) that the IT team must install.  
* **Where most students go wrong:** Students often confuse **Managerial** and **Operational** controls.  
  * **Managerial** is the *rule* or design (e.g., "The Policy states guards must check IDs").  
  * **Operational** is the *practice* or execution (e.g., The guard actually standing there checking the ID).  
  * *Exam Tip:* If it's a document or a decision by management, it's Managerial. If it's a recurring human task, it's Operational.  
* **Example Question:** **Scenario:** A Chief Information Security Officer (CISO) drafts a new Acceptable Use Policy (AUP) requiring all employees to sign an agreement before accessing the network. Which category of control does this policy represent?  
  * A. Technical  
  * B. Operational  
  * C. Managerial  
  * D. Corrective  
  * **Correct Answer: C.** Policies are high-level administrative decisions, making them Managerial.

**Control Types**

* **Control Type Explained:** Control types define the *function* or *timing* of the control relative to a security incident. When looking at a control, ask yourself: "Does this stop the attack, warn me about it, or fix the mess afterwards?"  
  * **Preventive:** Physically or logically stops an unauthorized activity from happening. Examples: Disabling a user account, a high fence, or an IPS (Intrusion Prevention System) blocking malicious traffic.  
  * **Deterrent:** Discourages an attacker by psychological means. It attempts to dissuade intrusion but may not physically stop it. Examples: "Warning: Trespassers will be prosecuted" signs, visible security cameras, or login banners warning of monitoring.  
  * **Detective:** Identifies and records that an intrusion is attempting or has occurred. It acts like a smoke alarm; it doesn't put out the fire, it just tells you there is one. Examples: Log files, SIEM alerts, and CCTV recordings (reviewed post-incident).  
  * **Corrective:** Mitigates damage *after* an incident has occurred to return systems to normal. Examples: Restoring data from backups, patching a vulnerability after a breach, or updating virus definitions.  
  * **Compensating:** An alternative control used when the primary control is too expensive or impossible to implement. Example: You cannot patch a legacy server (Primary), so you isolate it on its own VLAN (Compensating).  
  * **Directive:** A specific instruction on how to behave. These often overlap with Managerial controls. Example: Compliance standards or a "Do Not Enter" sign.  
* **How it connects to related concepts:** This connects to **Incident Response (4.8)**. Detective controls are what usually trigger the Identification phase of incident response, while Corrective controls are heavily used during the Eradication and Recovery phases.  
* **Where most students go wrong:**  
  * **Preventive vs. Deterrent:** A fence is Preventive (it physically blocks). A sign on the fence is Deterrent (it warns). A guard dog is both (it scares you *and* bites you).  
  * **Detective vs. Preventive:** A camera is usually **Detective** because you watch the footage *after* the crime. It only becomes Preventive if a guard is watching it live and can remotely lock a door.  
  * *Exam Tip:* If the question asks what control discourages an attacker without physically stopping them, the answer is always **Deterrent**.  
* **Example Question:** **Scenario:** During a security audit, it is discovered that a legacy application cannot support the encryption standards required by company policy. The security team decides to restrict access to this application to a specific VPN tunnel only accessible by authorized admins. What control type is this specific restriction?  
  * A. Detective  
  * B. Compensating  
  * C. Recovery  
  * D. Deterrent  
  * **Correct Answer: B.** Since the primary control (encryption) failed, the VPN restriction serves as a "safety net" or alternative measure, making it a Compensating control.