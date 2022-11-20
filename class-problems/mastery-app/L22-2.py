# Convert this to an accumulator loop to calculate cs15enrollments without a list comprehension...

cs15enrollments = [ 
         c['enrolled']
         for c in courses 
         if c['subject']=='COSI' 
            and c['term']=='Spring 2015' 
            and c['enrolled']>=50]