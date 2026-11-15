# UE23CS341A: Software Engineering — Lab 1
## Requirements Engineering & Use Case Modeling

**Student Name:** Vismay Shyam Vasishta  
**SRN:** PES2UG24AM184  
**PS:** 28  
**Department:** Computer Science and Engineering / AIML (5th Semester)  
**Institution:** PES University  

---

## 📌 Lab Overview & Objectives

The primary objective of **Lab 1** is to formulate formal software requirements and design a behavioral UML model for an assigned real-world software system:

* **Assigned System:** **Problem Statement #28 — Inter-City Freight Load Matching Marketplace**
* **System Summary:** A digital marketplace connecting commercial freight shippers with certified trucking carriers for inter-city cargo transportation, featuring auction-based bidding, automated carrier verification, milestone tracking with electronic proof-of-delivery (e-POD), and secure milestone escrow disbursement.

---

## 📂 Lab 1 Deliverables

| Deliverable | Description | File Format |
| :--- | :--- | :--- |
| **Deliverable 1** | Formal Requirements Engineering Specification (FRs & NFRs) | [Deliverable_1_Requirements_Table.pdf](Deliverable_1_Requirements_Table.pdf) |
| **Deliverable 2** | UML 2.5 Use Case Diagram (Actors, Use Cases & Relationships) | [Deliverable_2_UML_Use_Case_Diagram_Proper.pdf](Deliverable_2_UML_Use_Case_Diagram_Proper.pdf) |
| **Deliverable 3** | Detailed Use Case Flow Specification (*Release Milestone Payment*) | [Deliverable_3_Use_Case_Flow.pdf](Deliverable_3_Use_Case_Flow.pdf) |

---

## 📋 Deliverable 1: Requirements Engineering Specification

| Req ID | Type | Description | Priority | Acceptance Criteria | Rationale |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **FR-001** | Functional | The system shall allow verified trucking carriers to submit competitive bids on posted freight shipments within the specified auction timeframe. | High | **Pass:** Valid bid from verified carrier recorded and shipper notified.<br>**Fail:** Unverified carrier or bid submitted after auction closes is rejected. | Core auction functionality of the marketplace. |
| **FR-002** | Functional | The system shall allow shippers to create and publish freight shipment listings containing origin, destination, cargo details, weight, and required delivery schedule. | High | **Pass:** Shipment containing all mandatory fields successfully published.<br>**Fail:** System prevents publication if any mandatory field is missing. | Carriers require complete shipment parameters prior to bidding. |
| **FR-003** | Functional | The system shall allow a shipper to review submitted bids and select one eligible carrier for a shipment. | High | **Pass:** Selected carrier recorded and notified.<br>**Fail:** System prevents selection of unverified carrier or closed bid. | Enables shipper to evaluate and contract a carrier. |
| **FR-004** | Functional | The system shall allow the selected freight carrier to submit electronic proof of delivery (e-POD) after completing a shipment milestone. | High | **Pass:** Valid e-POD stored and forwarded for verification.<br>**Fail:** Invalid or incomplete e-POD rejected. | e-POD verification is a mandatory trigger for milestone escrow release. |
| **FR-005** | Functional | The system shall notify the shipper and freight carrier when important shipment events occur, including bid selection, e-POD verification, and payment release. | Medium | **Pass:** Real-time notifications dispatched for each specified event.<br>**Fail:** No notification generated on successful event execution. | Maintains visibility and transaction transparency for all parties. |
| **NFR-001** | Non-Functional | The system shall automatically disburse milestone payments held in escrow within 60 seconds of verified electronic proof-of-delivery submission. | High | **Pass:** Benchmarking confirms payment release within 60 seconds after valid e-POD verification under peak load.<br>**Fail:** Disbursement exceeds 60 seconds. | Guarantees fast, reliable liquidity for carriers upon milestone completion. |
| **NFR-002** | Non-Functional | The system shall protect shipment, bidding, and payment information from unauthorized access. | High | **Pass:** Unauthorized users denied access to protected data.<br>**Fail:** Any unauthorized entity accesses sensitive information. | Financial, commercial, and identity security is legally mandated. |

---

## 🎭 Deliverable 2: UML Use Case Diagram

### Primary Actors
1. **Shipper:** Commercial entity listing cargo shipments, evaluating bids, and tracking fulfillment.
2. **Freight Carrier:** Verified logistics operator submitting bids, moving shipments, and submitting milestone e-PODs.
3. **Escrow / Payment Service:** Financial system managing milestone escrow holds, validation, and automated payment disbursements.

### Core Use Cases & Relationships
* `Post Freight Shipment` (Shipper)
* `Submit Bid` (Freight Carrier) — `<<include>>` `Verify Carrier Eligibility`
* `Review & Select Carrier` (Shipper)
* `Submit e-POD` (Freight Carrier)
* `Verify e-POD` (System / Shipper)
* `Release Milestone Payment` (Escrow / Payment Service) — `<<include>>` `Verify e-POD`
* `Raise Delivery Dispute` (Shipper / Carrier) — `<<extend>>` `Verify e-POD`
* `Receive Notifications` (Shipper / Freight Carrier)

---

## 🔄 Deliverable 3: Use Case Flow Specification

* **Use Case:** **Release Milestone Payment**
* **Primary Actor:** Escrow / Payment Service
* **Supporting Actors:** Freight Carrier, Shipper

### Preconditions
1. Shipment posted and verified carrier selected (FR-001, FR-002, FR-003).
2. Shipment milestone completed by carrier.
3. Electronic proof of delivery (e-POD) submitted by carrier (FR-004).
4. Milestone payment held in secure escrow.

### Main Success Scenario (Happy Path)
1. Freight carrier submits electronic proof of delivery (e-POD).
2. System receives and timestamps the e-POD.
3. System verifies e-POD integrity and geolocation/signature data.
4. System confirms milestone completion status.
5. System requests Escrow / Payment Service to release milestone funds.
6. Escrow / Payment Service executes automated disbursement to the carrier.
7. System logs the financial transaction in the immutable audit repository.
8. System dispatches confirmation notifications to shipper and carrier.
9. Use case terminates successfully in compliance with the **60-second SLA (NFR-001)**.

### Alternate Flow — Invalid e-POD
1. At Step 3, if the e-POD verification fails, the system flags it as invalid.
2. Escrow release is halted; funds remain protected in escrow vault.
3. Carrier is notified of rejection with failure rationale.
4. Carrier is prompted to submit a corrected e-POD.
5. Use case ends without financial release.

---

## 🔗 Direct Continuity & Dependency with Lab 3

```
┌────────────────────────────────────────────────────────┐
│                        LAB 1                           │
│  Requirements Engineering & Use Case Behavioral Model  │
│  - Problem Statement #28 (Freight Load Marketplace)    │
│  - Requirements: FR-001 to FR-005, NFR-001, NFR-002   │
│  - Actors: Shipper, Freight Carrier, Escrow Service    │
│  - Use Cases: Bidding, e-POD, Escrow Milestone Release │
└───────────────────────────┬────────────────────────────┘
                            │
              Direct Structural Dependency
             (Requirements → Architecture)
                            ▼
┌────────────────────────────────────────────────────────┐
│                        LAB 3                           │
│   Component Modelling & Architectural Pattern Choice   │
│  - Layered Architecture Selection & Justification      │
│  - UML 2.5 Component Diagram (6 components, 3 layers)  │
│  - Modules directly implementing Lab 1 Use Cases:      │
│    • Shipment Order Manager Component (FR-002, FR-003) │
│    • Carrier Bidding & Matching Component (FR-001)     │
│    • e-POD Verification Service Component (FR-004)     │
│    • Escrow & Payment Service Component (NFR-001)      │
│    • Secure Database & Audit Repository (NFR-002)      │
└────────────────────────────────────────────────────────┘
```

Because **Lab 3** directly implements the architectural blueprint for the requirements defined in **Lab 1**, all Lab 3 assets reside in the subfolder:

👉 **[Go to Lab 3 Deliverables & Architecture Documentation](Lab%203/README.md)**

---

## 🎓 Academic Integrity & Authorship
This submission represents original academic work completed by **Vismay Shyam Vasishta (SRN: PES2UG24AM184)** for **UE23CS341A: Software Engineering**, Department of Computer Science & Engineering, PES University.
