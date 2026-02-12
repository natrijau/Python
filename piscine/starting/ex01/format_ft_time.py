from datetime import datetime, timezone

post_date = datetime(1970, 1, 1, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)

delta = now - post_date
#print("\n","La valeur de post_date :", post_date, ", et de now :", now,"\n","La difference delta = ", delta, "\n")
seconds = delta.total_seconds()
#print("\n", "seconds = ", seconds, "\n")

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")

date_str = now.strftime("%b %d %Y")
print(date_str)
