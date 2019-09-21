

    $('.responsive').slick({
        // dots: true,
        prevArrow: $(".prev"),
        nextArrow: $(".next"),
        infinite: true,
        speed: 300,
        autoplay: true,
        autoplaySpeed: 2000,
        slidesToShow: 4,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 5,
                    slidesToScroll: 1,
                    infinite: true,
                    // dots: true,
                    speed: 300,
                    autoplay: true,
                    autoplaySpeed: 2000,
                    prevArrow: $(".prev"),
                    nextArrow: $(".next"),

                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

    console.log("hello world 4545");

