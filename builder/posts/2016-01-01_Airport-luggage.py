def get_post():
  from templates.post_template import create_blog_post
  from elements.YtVideo import get_yt_video
  
  return create_blog_post(
    page_title='What you can\'t take on a plane',
    thumb_path='Airport-luggage',
    post_date='2016-01-07',
    categories=['travel_advice', 'voylins_life'],
    description= """
    So you are about to go on a trip but you are not sure what exactly you can take on the plane with you, well look no further as I have made a handy video talking about this subject! Or you can just read the list below. :p""",
    content=f"""
{get_yt_video('lcroxN_eDd4')}
<h1>Airport luggage</h1>
<p>So you are about to go on a trip but you are not sure what exactly you can take on the plane with you, well look no further as I have made a handy video talking about this subject! Or you can just read the list below. :p</p>
<h2>Special requirements for carry-on luggage:</h2>
<h3>Lithium Batteries</h3>
<p>Large lithium batteries need to be put in a non-electrostatic bag and contacts must be covered by non-conducting tape.</p>
<h3>Liquids</h3>
<p>Liquids should be in bottles of 100ml and be put in a ziplock 1L, or smaller, plastic bag. One person = One bag.</p>
<p>There are of course some exceptions:</p>
<ul>
  <li>Baby food;</li>
  <li>Diet food;</li>
  <li>Medicine.</li>
</ul>
<p>These are only allowed when they will be consumed during the flight.</p>
<h3>Electronic devices</h3>
<p>In some countries, they will check if your electronic devices are all working. Requirements: Being able to switch on and be operational.</p>
<h3>Self-balancing devices</h3>
<p>These are straight up, not allowed. Pulling out the battery doesn't help, I think it's the fault of the cheap knockoffs which are known for being fire hazards.</p>
<h3>Artificial cigarettes</h3>
<p>They are allowed but only in your carry on luggage. Of course, you are still not able to use them at the airport or on the plane, only in the smoking rooms (if available).</p>
<h3>Animal origin products</h3>
<p>Living, dead, or parts of animals aren't allowed in check-in, nor carry on. You need to have special permission to take a live animal with you on the plane or as check-in luggage. Be sure to request information at your airline company in advance and when going to a country outside of yours, be sure to get all needed vaccinations.</p>
<p>There is one exception: Baby food with animal products inside, but again, only when being consumed during the flight.</p>
<h3>Fire-arms</h3>
<p>Not allowed in carrying on, real ones or fakes like a Nerf gun. Take them in your check-in luggage. For real firearms, you will however need special permission.</p>
<h3>Sharp or blunt objects</h3>
<p>Again, not allowed as carry-on luggage. You can have permission to take it in your checked luggage. Please check which objects you are allowed to take out of the country before buying them as a gift or souvenir as you may end up not being allowed to take it home with you.</p>
<p>A skateboard is also considered as a blunt object so according to its size, they will determine if it's allowed or not as carry on.</p>
<h2>You don't need grenades or fireworks on vacation</h2>
<p>This one surprised me when I found out about how many fireworks/grenades are being taken at airports by people who were going on vacation. Please tell me, why do you need them during your holiday?</p>
<p>Chemical and Toxic products are also not allowed, anything that can harm other people like Acids or nuclear material is something you really should think over, why you actually have those things.</p>
""")