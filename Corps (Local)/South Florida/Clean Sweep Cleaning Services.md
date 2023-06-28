Clean Sweep Cleaning Services is a professional cleaning company that offers a range of cleaning solutions for residential and commercial properties. They provide thorough and efficient cleaning services, including regular maintenance, deep cleaning, and specialized cleaning for specific needs. Clean Sweep Cleaning Services is committed to delivering a spotless and hygienic environment for their clients.

```mermaid
---
title: "Arma 3 - Basic Medical in ACE" 
---
flowchart TD 
	977290(["Unresponsive patient"]) --> 289944{"Is their body ragdolled or limp?"}
	289944 -->|"Yes"| 227197("Patient ded") 
	289944 -->|"No"| 335680{"Lost more than #quot;some#quot; blood?"} 
	335680 -->|"No"| 122890("Inject Epinephrine") 
	335680 -->|"Yes"| 623814("Stop the bleeding.\nRefer to Bleeding guide") 
	122890 --> 623814 
	623814 --> 549744("Transfuse blood.\nRefer to transfusion guide") 
	549744 --> 682444("Fully bandage all limbs") 
	682444 --> 109205("Remove tourniquets") 
	109205 --> 263334{"Lost more than #quot;some#quot; blood?"} 
	263334 -->|"Yes"| 644629("Wait for transfusion") 
	644629 --> 263334 
	263334 -->|"No"| 432937{"Patient still unconscious?"} 
	432937 -->|"Yes"| 829784("Inject Epinephrine") 
	432937 -->|"No"| 601555(["Alive!"])
```

