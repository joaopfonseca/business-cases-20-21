# BC2: Predict Hotel Booking Cancellations

**Problem type:** Classification

**Submission date:** 15-March-2021 | 11.59pm

## General Context

In the hotel industry, as in many other travel-related industries, demand is
managed through advanced bookings. Bookings (also known as reservations) are a
forward contract between the hotel and the customer that gives the customer
the right to use the service in the future at a settled price, but often with
an option to cancel [^1]. This cancellation option puts the risk on hotels who
have to honor the bookings that they have on-the-books, but, at the same time,
have to support the opportunity costs of having vacant rooms, when someone
cancels, and there is no time to try to sell the room or sell it at a
discounted price. In Europe, the cancellation rate by reservation value, from
2014 to 2018, rose from 33% to 40% [^2].

Cancellations occur for understandable reasons such as business meeting
changes, vacations rescheduling, illness, or adverse weather conditions.
However, cancellations also occur for not so understandable reasons, such as
finding a better deal. “Deal-seeking” customers, tend to make multiple
bookings for the same trip or make one booking, but continue to search for
better deals (e.g., looking for hotels with better social reputation, better
price, or better location) [^4]. The number of “deal-seeking” customers has
grown immensely with the appearance of Online Travel Agencies (OTAs) in 1996
[^2,5].

Although OTAs provide high market exposure and the possibility of hotels for
selling inventory at opaque and bundled rates, they also have negative
aspects. OTAs charge commissions that range from 15% to 30%. OTAs force hotels
to guarantee to them the best available price or force rate parity among the
different distribution channels.  Due to the exposure that hotels gained with
OTAs and online distribution, competition is fierce among hotels. This
competition, together with OTAs push for hotels to practice a free
cancellation policy [^2], makes hotels employ controls such as overbooking to
fight cancellations. However, overbooking creates several problems:

- **Reallocation costs:** hotels must pay for the reallocation of customers in other hotels;
- **Social reputation damage:** customers sharing their unpleasant experience in social media, harm the hotel social reputation;
- **Loss of immediate and future revenue:** hotels lose not only the revenue of the reallocated customer current booking but also the possible future revenue of that customer, as probably, the customer will not want to book again at the hotel.

On the other side, restrictive cancellation policies, such as non-refundable
rates, also create problems:

- **A decrease in revenue:** due to the discounts on prices;
- **A decrease in the number of bookings:** as most customers do not like these type of policies.

## Business Situation

Hotel chain C, a chain with resort and city hotels
in Portugal, isn't any different than other independent and
non-independent hotel chains. Hotel chain C was severely impacted by
cancellations, representing almost 28% in H1 and almost 42% in H2, as shown in
the table below. For this
reason, Michael,
Revenue Manager Director of hotel chain C, decided to limit the number of rooms sold with restrictive
cancellation policies. To balance that decision, Michael implemented a more
aggressive overbooking policy. However, the latter started to generate costs.
To counterbalance those costs, Michael softened the overbooking policy, which in
turn also revealed to be not good. The less aggressive overbooking policy
resulted in the hotel having inventory not sold, even on high demand dates.

| Hotel | Metric       | Not Canceled        | Canceled            | Total              |
|-------|--------------|---------------------|---------------------|--------------------|
| H1    | Bookings     | 28,938 (72.2%)      | 11,122 (27.8%)      | 40,060 (100%)      |
| H1    | Room Revenue | 11,601,850€ (66.5%) | 5,842,177€ (33.5%)  | 17,444,028€ (100%) |
| H2    | Bookings     | 46,228 (58.3%)      | 33,102 (41.7%)      | 79,330 (100%)      |
| H2    | Room Revenue | 14,394,410€ (56.9%) | 10,885,060€ (43.1%) | 25,279,470€ (100%) |

Concerned about the increasingly negative impact caused by cancellations,
Michael hired a consultant to evaluate the possibility of developing
predictive models to predict the net demand for their hotels, specifically in
a city hotel (H2). The hotel provided the consultant a dataset with the
bookings made in that hotel, which were due to arrive between July 1, 2015,
and August 31, 2017 [^3].

To reduce the uncertainty about demand, Michael wants to implement prediction
models to allow the chain’s hotels to forecast net demand based on
reservations on-the-books. With these models' estimations, Michael expects to
implement better pricing and overbooking policies and identify bookings with
high likelihood of canceling. Identifying those bookings could allow the
hotels to try to contact those bookings’ customers and make offers to try to
prevent cancellation (e.g., dinner, car parking, spa treatments, discounts, or
other perks). Michael's goal is to reduce cancellations to a rate of 20%.

## Metadata

| Name                        | Meaning                                                                                                                                                                                                                                                          |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADR                         | Average Daily Rate                                                                                                                                                                                                                                               |
| Adults                      | Number of adults                                                                                                                                                                                                                                                 |
| Agent                       | ID of the travel agency that made the booking                                                                                                                                                                                                                    |
| ArrivalDateDayOfMonth       | Day of the month of the arrival date                                                                                                                                                                                                                             |
| ArrivalDateMonth            | Month of arrival date with 12 categories:  “January” to “December”                                                                                                                                                                                               |
| ArrivalDateWeekNumber       | Week number of the arrival date                                                                                                                                                                                                                                  |
| ArrivalDateYear             | Year of the arrival date                                                                                                                                                                                                                                         |
| AssignedRoomType            | Code for the type of room assigned to the booking. Sometimes the assigned room type differs from the reserved room type due to hotel operation reasons (e.g. overbooking) or by customer request. Code is presented instead of designation for anonymity reasons |
| Babies                      | Number of babies                                                                                                                                                                                                                                                 |
| BookingChanges              | Number of changes/amendments made to the booking from the moment the booking was entered on the PMS until the moment of check-in or cancellation                                                                                                                 |
| Children                    | Number of children                                                                                                                                                                                                                                               |
| Company                     | ID of the company/entity that made the booking or responsible for paying the booking. ID is presented instead of designation for anonymity reasons                                                                                                               |
| Country                     | Country of origin. Categories are represented in the ISO 3155-3:2013 format                                                                                                                                                                                      |
| CustomerType                | Type of booking, assuming one of four possible categories (presented below)                                                                                                                                                                                      |
| DaysInWaitingList           | Number of days the booking was in the waiting list before it was confirmed to the customer                                                                                                                                                                       |
| DepositType                 | Indication on if the customer made a deposit to guarantee the booking. This variable can assume three categories (presented)                                                                                                                                     |
| DistributionChannel         | Booking distribution channel. The term “TA” means “Travel Agents” and “TO” means “Tour Operators”                                                                                                                                                                |
| IsCanceled                  | Value indicating if the booking was canceled (1) or not (0)                                                                                                                                                                                                      |
| IsRepeatedGuest             | Value indicating if the booking name was from a repeated guest (1) or not (0)                                                                                                                                                                                    |
| LeadTime                    | Number of days that elapsed between the entering date of the booking into the PMS and the arrival date                                                                                                                                                           |
| MarketSegment               | Market segment designation. In categories, the term “TA” means “Travel Agents” and “TO” means “Tour Operators”                                                                                                                                                   |
| Meal                        | Type of meal booked. Categories are presented in standard hospitality meal packages (presented below)                                                                                                                                                            |
| PreviousBookingsNotCanceled | Number of previous bookings not cancelled by the customer prior to the current booking                                                                                                                                                                           |
| PreviousCancellations       | Number of previous bookings that were cancelled by the customer prior to the current booking                                                                                                                                                                     |
| RequiredCarParkingSpaces    | Number of car parking spaces required by the customer                                                                                                                                                                                                            |
| ReservationStatus           | Reservation last status, assuming one of three categories (presented below)                                                                                                                                                                                      |
| ReservationStatusDate       | Date at which the last status was set. This variable can be used in conjunction with the ReservationStatus to understand when was the booking canceled or when did the customer checked-out of the hotel                                                         |
| ReservedRoomType            | Code of room type reserved. Code is presented instead of designation for anonymity reasons                                                                                                                                                                       |
| StaysInWeekendNights        | Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel                                                                                                                                                                    |
| StaysInWeekNights           | Number of weeknights (Monday to Friday) the guest stayed or booked to stay at the hotel                                                                                                                                                                          |
| TotalOfSpecialRequests      | Number of special requests made by the customer (e.g. twin bed or high floor)                                                                                                                                                                                    |


**CustomerType** categories:
- Contract - when the booking has an allotment or other type of
- contract associated to it;
- Group – when the booking is associated to a group;
- Transient – when the booking is not part of a group or contract, and is not associated to other transient booking;
- Transient-party – when the booking is transient, but is associated to at least other transient booking

**DepositType** categories:
- No Deposit – no deposit was made;
- Non Refund – a deposit was made in the value of the total stay cost;
- Refundable – a deposit was made with a value under the total cost of stay.

**Meal** categories:
- Undefined/SC – no meal package;
- BB – Bed & Breakfast;
- HB – Half board (breakfast and one other meal – usually dinner);
- FB – Full board (breakfast, lunch and dinner)

**ReservationStatus** categories:
- Canceled – booking was canceled by the customer;
- Check-Out – customer has checked in but already departed;
- No-Show – customer did not check-in and did inform the hotel of the reason why


## Additional Remarks

- Additional metadata can be found in the supplementary paper.
- The name of the individuals and company involved are anonymized to protect
confidentiality. Although, the data set provided comes from a real business.
- Net demand is defined as demand minus cancellations.

## Expected Outcomes

1. Explore the data and build a model to predict cancellations:
    * Define a machine learning success criteria;
    * Take in consideration the business objectives and requirements when selecting the algorithm;
2. Elaborate on the business implications of employing the model and the insights obtained from model development
3. Make suggestions how could the model be deployed and its impact on the hotel’s business processes

## References

[^1]: TALLURI, Kalyan T. and VAN RYZIN, Garrett. The theory and practice of revenue management. New York, NY : Springer, 2005. International series in operations research & management science, 68. ISBN 1-4020-7701-7.
[^2]: HERTZFELD, Esther. Study: Cancellation rate at 40% as OTAs push free change policy. Hotel Management [online]. April 23 2019. [Accessed August 15 2019]. Available from: https://www.hotelmanagement.net/tech/study-cancelation-rate-at-40-as-otas-push-free-change-policy
[^3]: ANTONIO, Nuno, ALMEIDA, Ana de and NUNES, Luis. Hotel booking demand datsets. Data in Brief. February 2019. Vol. 22, p. 41–49. DOI 10.1016/j.dib.2018.11.126.
[^4]: ANTONIO, Nuno, DE ALMEIDA, Ana and NUNES, Luis. Big Data in hotel Revenue Management: Exploring cancellation drivers to gain insights Into booking cancellation behavior. Cornell Hospitality Quarterly. May 29 2019. P. 193896551985146. DOI 10.1177/1938965519851466.
[^5]: BARTHEL, Jill and PERRET, Sophie. OTAs – A hotel’s friend or foe? [online]. London, UK : HVS, 2015. Available from: https://www.hospitalitynet.org/file/152005663.pdf
