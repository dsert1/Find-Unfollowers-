import instapy
from instapy import InstaPy
from instapy.util import smart_run
import instapy
from credentials import username, password


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=username,
                  password=password,
                  headless_browser=False)

def find_unfollowers(followers, following):
    return {unfollower for unfollower in following if unfollower not in followers}

with smart_run(session):
    """ Activity flow """
    # settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # actions
    # session.like_by_tags(["natgeo"], amount=10)
    followers = session.grab_followers(username='denizsert_', amount='full', live_match=True, store_locally=True)
    following = session.grab_following(username='denizsert_', amount='full', live_match=True, store_locally=True)

    # print('followers: ', followers)
    # print('following: ', following)
    unfollowers = find_unfollowers(followers, following)
    print(unfollowers)



