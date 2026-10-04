> SYNTHETIC SAMPLE for secure-agent-ops. Not real data. The company, people, vendor, and domains (example.com) are fictional.

# AI use case intake form

**Company:** Brightpath Outfitters (fictional), online retailer
**Submitted:** 2026-09-29 by Lucia Ferrante (fictional), Digital Customer Experience
**System name:** Order Help Chat ("Sam")
**Inventory ID:** AI-INV-0063
**New or expansion:** New

## 1. Owners
- Business owner: Lucia Ferrante (fictional), Director of Digital Customer Experience
- Technical owner: Ken Watanabe (fictional), E-commerce Engineering
- Risk approver: AI Governance Council

## 2. Purpose and users
A chat assistant on `www.brightpath.example.com` that answers order questions for signed-in
customers: order status, returns, delivery dates, and updating the shipping address on orders
that haven't shipped. Answers come from the help center and the customer's own orders.
About 40,000 chats a month expected. Customers in the US, UK, and EU.

Out of scope: payments, refunds over $200 (handed to a human), account deletion.

## 3. Self-assessed risk
Medium.

## 4. Model and vendor
Hosted model from ModelCo (fictional) via our enterprise account. DPA signed 2026-05-02
(attached): no training on our data, 0-day retention for API traffic, EU data processing
available and enabled for EU customers.

## 5. Data
- Customer name, email, shipping addresses, order history, and the last 4 digits of the card
  on file (shown in order details).
- Help-center articles (retrieval index, rebuilt nightly).
- Chat transcripts kept 1 year for quality review.

## 6. Tools and permissions
- `orders.read` (signed-in customer's own orders only, enforced by session token)
- `orders.update_shipping_address` (unshipped orders; customer must confirm the new address
  in a confirmation dialog)
- `handoff.create` (to a human agent)

## 7. Testing
- Answer quality: 500 historical questions, 91% rated correct by support leads (report attached).
- Security: tested that one customer can't see another's orders (passed). Prompt-injection
  testing through help-center content and customer messages is planned for 2026-10-15.

## 8. Human oversight
Customer confirms any address change. Human handoff on request or when the assistant is unsure.
Support leads review 2% of transcripts weekly.

## 9. Transparency and training
The assistant is called "Sam" with a friendly avatar. We don't plan to say it's AI because
testing showed customers prefer talking to "a person". Support staff trained 2026-09-20.

## 10. Policy fit
AI Acceptable Use Standard v2.0, section 5: customer-facing AI requires Governance Council approval (this request).

## 11. Monitoring and incidents
Dashboards for containment rate, handoffs, and CSAT. Feature flag can disable chat in minutes.
No AI incident definition yet.

## 12. Legal and privacy
Privacy impact assessment in progress (draft attached, not signed). Legal review not requested yet.

## 13. Change management
New tools or new data need a new review.

## 14. Decommissioning
Feature flag off; transcripts deleted per retention.
