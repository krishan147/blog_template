def EachWork():

    allWork = [
                {
                    'title':"Live dash barchart",
                    'date':"2019-04-10",
                    "content_type": "frame",
                    "content":"http://20180410forexlivebarchart2.us-east-2.elasticbeanstalk.com/",
                    "notes": "Made a bar chart in dash with live Forex data on the value of the USD against the GBP, EUR, KWD, CHF, CAD and ZAR. Using iframe to show this chart becuase I'm still trying to figure out how to embed dash charts in flask. Here is a link to the repo",
                    "repo": "https://github.com/krishan147/forexlive/",
                },
        {
            'title': "Geographic Heatmap",
            'date': "2019-04-08",
            "content_type": "frame",
            "content": "http://geographicheatmap8.us-east-2.elasticbeanstalk.com/",
            "notes": "Made a geographic heatmap using the folium library. Data is currently sample data. Want to make one with live data. Here is a link to the repo: ",
            "repo": "https://github.com/krishan147/geographic_heatmap",
        },

        {
            'title': "Four-dimensional heatmap",
            'date': "2019-04-05",
            "content_type":"image",
            "content": "static/images/20180405_heatmap.png",
            "notes": "Done in Python but doesn't look as pretty in comparison to R & ggplot. Here is a link to the repo: ",
            "repo":"https://github.com/krishan147/four_dimensional_heatmap"
        }

    ]

    return allWork