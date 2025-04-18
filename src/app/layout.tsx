export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">

      <head>
        <title>CRAMMASTER.AI</title>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      </head>

      <body>
        <main>{children}</main>
      </body>
    </html>
  )
}