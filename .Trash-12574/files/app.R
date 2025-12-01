# This is a sample R/Shiny script to show Domino's App publishing functionality
#   learn more at http://support.dominodatalab.com/hc/en-us/articles/209150326

server <- function(input, output) {
  output$distPlot <- renderPlot({
    hist(rnorm(input$obs), col = 'darkgray', border = 'white')
  })
  output$output_text <- renderText({
    paste(system2("find", "/mnt/data", stdout=TRUE, stderr=TRUE), collapse=", ")
  })

 }

ui <- fluidPage(sidebarLayout(sidebarPanel(
  sliderInput(
    "obs", "Number of observations:", min = 10, max = 500, value = 100
  )
),

mainPanel(textOutput("output_text"))))

shinyApp(ui = ui, server = server)
