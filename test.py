# def estimate_speech_duration(text, wpm=206):
#     words = text.split()
#     num_words = len(words)
#     minutes = num_words / wpm
#     seconds = minutes * 60
#     return seconds

# def calculate_speed_adjustment(estimated_duration, target_duration):
#     return estimated_duration / target_duration

# s = """My sister is a god damn mess, she was a lot growing up and each week some issue would appear. The could be as simple as a tantrum, or mom/dad getting a call from the school.

# I’m short she was a lot. Not to mention therapy for her basically drained the family dry. I was giving more freedom since my parents trusted me. I could go to mall by myself and they knew they wouldn’t get a call from security about stealing. That happened before.

# So they trusted me and gave me more freedom to do stuff. I have literally watch her get a chance to prove our parents can trust her and then fuck it up.

# Our relationship isn’t good. My dad gave me his old car for my last year of college. I need it for an internship. My sister made a comment that of course the golden child gets a car.

# I snapped and told her I am not the golden child I just wasn’t a pain in the ass. That the fmaily has drained themselves dry for her multiple time and to keep her mouth shut.

# She called me a jerk and ran to her room."""
# a = estimate_speech_duration(s)
# print(a)
# print(calculate_speed_adjustment(a, 55))
p = "AMITA asdad AITA"
print(p.replace("AMITA", "asd").replace("AITA", "asd"))