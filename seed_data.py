from SocialTravel.models import post

for posts in range(0,10):
    post(carousel_caption_title = "A carousel title",
        carousel_caption_description = "A carousel description",
        heading = "A heading",
        description = "A description").save()
    
    


