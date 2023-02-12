# Content Based Image Retrieval
By evaluating the color and texture similarities of the pictures, a system was created to find the 5 most similar pictures to a picture.

Only the color and texture similarities are calculated with the Manhattan City Block (L1 norm) method, and the 5 most similar images to the entered image are found.

The output of the program is given in the figure below.

<img src="https://user-images.githubusercontent.com/46672488/218333363-f48966a3-1fa8-4a1e-bd82-b2509553cd76.png" width="480">

## Performance Analysis
It was considered successful if at least one of the 5 predicted images belonged to the class of the test image. The success rate is calculated according to the pictures in the `database/test` folder.

| Class | RGB | LBP |
| ----- | :-: | :-: |
| Accordion | 100% | 100% |
| Dalmatian | 70% | 70% |
| Dolphin | 80% | 80% |
| Leopards | 90% | 90% |
| Schooner | 60% | 90% |
| Water Lily | 40% | 100% |
| Wild Cat | 80% | 70% |
| **Total** | **74.28%** | **85.71%** |

The percentage of success in calculating distance according to RGB values was very good for the accordion. Because the accordion pictures in the database are clear and close pictures. Thus, the similarity of the colors was high. However, this is not the case for the water lily. The colors of some of the flowers in the water lily pictures in the database are different. Therefore, the success rate is low.

The percentage of success in calculating distance according to LBP values is generally good.

Looking at the overall success percentages, it seems that LBP distance is higher than RGB. The reason for this is that the same object may appear in different colors in the pictures due to various factors or, for example, a flower may have other colors. Therefore, the success rate in terms of color is lower than texture.
