ამ მინი პროექტში ნასას API-ის, კერძოდ კი asteroids Api-ს გამოყენებით წარმოდგენილია ინფორმაცია 
დედამიწასთან ახლოს გარკევულ დღეს აღმოჩენილ ასტეროიდებზე. 
გამოყენებულია ორი მოდული: requests და json და მათი ზოგიერთი ფუნქცია. 
აგრეთვე პროექტში წარმოდგენილიამონაცემთა ბაზასთან დაკავშირება sqlite3 მოდულის გამოყენებით.
დეტალური ინფორმაცია მოცემულია main ფაილში კომენტარების სახით.

პროგრამული ენა: Python



README.md for parsin quiz:
მეორე მინი პროექტში, რომელიც ეხება Parsing-ს, request და BeautifulSoup მოდულების სხვადასხვა მეთოდების გამოყენებით 
საიტიდან სახელად myanimelist წამოღებულია 250 ყველაზე პუპულარული ანიმეები, მათი რანკები(ადგილი სიაში) და რეიტინგი. 
წამოღებული ინფორმაცია CSV მოდულის გამოყენებით შენახულია csv ფაილში. 
STEPS:
1. აღებულია საიტის url-ს
2. request მოდულის get მეთოდით შემოწმებულია response.
3. ვხსნი csv ფაილს.
4. writerow მეთოდით სვეტებს ვანიჭებ შესაბამის სახელებს
5. while ციკლში(რომელიც მანამ შესრულდება სანამ url-ის limit პარამეტრი ნაკლები იქნება 250-ზე), get მეთოდით წამოღებული
რესფონსის ტექსტი ხდება beautifulsoupis ობიექტი. 
6. მიღებულ ობიექტზე უკვე შეიძლება find და find_all მეთოდების გამოყენება, რითაც html-ში ვიპოვით სასურველ ინფორმაციას.
7. for ციკლში კი უკვე კონკრეტულად სახელს, რანკსა და რეიტინგს წამოვიღებთ html-იდან. რამდენიმე ანიმეს სახელში იყო სხვადასხვა სიმბოლოები,
რომლებსაც ვერ აღიქვამდა პროგრამა და ისინი replace მეთოდით ჩავანაცვლე ცარიელი სტრიქონებით.
8. csv ფაილის f ობიექტში writerow მეთოდით ჩავწერე შესაბამისი ცვლადების მნიშვნელობები.
9. ბოლოს კი გამოყენებულია sleep და random მოდული, რათა ყოველი შემდეგი 50 ანიმეს შესახებ ინფორმაცია არა იმავე წამს, არამმედ გარკვეული დროის შემდეგ იქნას წამოღებული.


რ
