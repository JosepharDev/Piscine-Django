#!/bin/python3
import sys
import antigravity

def main():
    """
    Geohashing program that calculates a geohash based on input parameters.
    Expected arguments: latitude longitude date dow_jones_value
    """
    if len(sys.argv) != 5:
        print("Error: Insufficient arguments")
        print("Usage: python geohashing.py <latitude> <longitude> <date> <dow_jones>")
        sys.exit(1)
    
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date = sys.argv[3]
        dow_jones = sys.argv[4]
        
        if not (-90 <= latitude <= 90):
            print("Error: Latitude must be between -90 and 90")
            sys.exit(1)
        
        if not (-180 <= longitude <= 180):
            print("Error: Longitude must be between -180 and 180")
            sys.exit(1)
        
        datedow = f"{date}-{dow_jones}".encode()
        antigravity.geohash(latitude, longitude, datedow)
        
    except ValueError as e:
        print(f"Error: Invalid numeric value - {e}")
        sys.exit(1)
    except AttributeError:
        print("Error: geohash function not available in antigravity module")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()