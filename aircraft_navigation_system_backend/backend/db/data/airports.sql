DELETE FROM Airports;
INSERT INTO Airports (airport_id, airport_name, city, country, IATA_code, latitude, longitude)
VALUES
(1, 'Hartsfield-Jackson Atlanta International Airport', 'Atlanta', 'USA', 'ATL', 33.6407, -84.4279),
(2, 'Beijing Capital International Airport', 'Beijing', 'China', 'PEK', 40.0801, 116.5846),
(3, 'Dubai International Airport', 'Dubai', 'UAE', 'DXB', 25.2532, 55.3657),
(4, 'Los Angeles International Airport', 'Los Angeles', 'USA', 'LAX', 33.9416, -118.4085),
(5, 'Tokyo Haneda Airport', 'Tokyo', 'Japan', 'HND', 35.5494, 139.7798),
(6, 'London Heathrow Airport', 'London', 'UK', 'LHR', 51.4700, -0.4543),
(7, 'Shanghai Pudong International Airport', 'Shanghai', 'China', 'PVG', 31.1433, 121.8057),
(8, 'Hong Kong International Airport', 'Hong Kong', 'Hong Kong', 'HKG', 22.3080, 113.9140),
(9, 'Paris Charles de Gaulle Airport', 'Paris', 'France', 'CDG', 49.0097, 2.5477),
(10, 'Amsterdam Schiphol Airport', 'Amsterdam', 'Netherlands', 'AMS', 52.3770, 4.9009),
(11, 'Changi Airport', 'Singapore', 'Singapore', 'SIN', 1.3644, 103.9915),
(12, 'Dallas/Fort Worth International Airport', 'Dallas/Fort Worth', 'USA', 'DFW', 32.8998, -97.0403),
(13, 'Guangzhou Baiyun International Airport', 'Guangzhou', 'China', 'CAN', 23.3923, 113.2995),
(14, 'Istanbul Airport', 'Istanbul', 'Turkey', 'IST', 41.2753, 28.7519),
(15, 'Incheon International Airport', 'Seoul', 'South Korea', 'ICN', 37.4600, 126.4407),
(16, 'Chhatrapati Shivaji International Airport', 'Mumbai', 'India', 'BOM', 19.0886, 72.8656),
(17, 'Singapore Changi Airport', 'Singapore', 'Singapore', 'SIN', 1.3644, 103.9915),
(18, 'Denver International Airport', 'Denver', 'USA', 'DEN', 39.8561, -104.6737),
(19, 'Soekarno-Hatta International Airport', 'Jakarta', 'Indonesia', 'CGK', -6.1256, 106.6559),
(20, 'O’Hare International Airport', 'Chicago', 'USA', 'ORD', 41.9742, -87.9073),
(21, 'Madrid Barajas International Airport', 'Madrid', 'Spain', 'MAD', 40.4722, -3.5600),
(22, 'Rome Fiumicino Airport', 'Rome', 'Italy', 'FCO', 41.8003, 12.2389),
(23, 'Miami International Airport', 'Miami', 'USA', 'MIA', 25.7959, -80.2870),
(24, 'Kuala Lumpur International Airport', 'Kuala Lumpur', 'Malaysia', 'KUL', 2.7456, 101.7213),
(25, 'Mexico City International Airport', 'Mexico City', 'Mexico', 'MEX', 19.4363, -99.0719),
(26, 'JFK International Airport', 'New York', 'USA', 'JFK', 40.6413, -73.7781),
(27, 'Moscow Sheremetyevo International Airport', 'Moscow', 'Russia', 'SVO', 55.9726, 37.4146),
(28, 'Hamad International Airport', 'Doha', 'Qatar', 'DOH', 25.2764, 51.5650),
(29, 'Chengdu Shuangliu International Airport', 'Chengdu', 'China', 'CTU', 30.5780, 103.9480),
(30, 'Bangkok Suvarnabhumi Airport', 'Bangkok', 'Thailand', 'BKK', 13.6810, 100.7470),
(31, 'Suvarnabhumi Airport', 'Bangkok', 'Thailand', 'BKK', 13.6810, 100.7470),
(32, 'Bangkok Don Mueang International Airport', 'Bangkok', 'Thailand', 'DMK', 13.9125, 100.6070),
(33, 'São Paulo–Guarulhos International Airport', 'São Paulo', 'Brazil', 'GRU', -23.4356, -46.4731),
(34, 'Frankfurt Airport', 'Frankfurt', 'Germany', 'FRA', 50.1109, 8.6821),
(35, 'Minneapolis–Saint Paul International Airport', 'Minneapolis', 'USA', 'MSP', 44.8833, -93.2216),
(36, 'Ataturk Airport', 'Istanbul', 'Turkey', 'IST', 40.9778, 28.8157),
(37, 'Fukuoka Airport', 'Fukuoka', 'Japan', 'FUK', 33.5850, 130.4506),
(38, 'Adolfo Suárez Madrid–Barajas Airport', 'Madrid', 'Spain', 'MAD', 40.4731, -3.5600),
(39, 'Dubai World Central', 'Dubai', 'UAE', 'DWC', 25.2532, 55.3657),
(40, 'Shenzhen Bao’an International Airport', 'Shenzhen', 'China', 'SZX', 22.6398, 113.8102),
(41, 'Bali Ngurah Rai International Airport', 'Denpasar', 'Indonesia', 'DPS', -8.7482, 115.1677),
(42, 'Tokyo Narita Airport', 'Tokyo', 'Japan', 'NRT', 35.7721, 140.3860),
(43, 'Delhi Indira Gandhi International Airport', 'Delhi', 'India', 'DEL', 28.5562, 77.1000),
(44, 'Vancouver International Airport', 'Vancouver', 'Canada', 'YVR', 49.1947, -123.1830),
(45, 'Los Angeles International Airport', 'Los Angeles', 'USA', 'LAX', 33.9416, -118.4085),
(46, 'Nairobi Jomo Kenyatta International Airport', 'Nairobi', 'Kenya', 'NBO', -1.319167, 36.9275),
(47, 'Ethiopia Bole International Airport', 'Addis Ababa', 'Ethiopia', 'ADD', 9.0319, 38.7403),
(48, 'Lima Jorge Chávez International Airport', 'Lima', 'Peru', 'LIM', -12.0219, -77.1147),
(49, 'Lagos Murtala Muhammed International Airport', 'Lagos', 'Nigeria', 'LOS', 6.5775, 3.3231),
(50, 'Jakarta Soekarno-Hatta Airport', 'Jakarta', 'Indonesia', 'CGK', -6.1256, 106.6559),
(51, 'Jeddah King Abdulaziz International Airport', 'Jeddah', 'Saudi Arabia', 'JED', 21.6773, 39.1541),
(52, 'Osaka Kansai International Airport', 'Osaka', 'Japan', 'KIX', 34.4278, 135.2444),
(53, 'Berlin Brandenburg Airport', 'Berlin', 'Germany', 'BER', 52.3667, 13.5033),
(54, 'Lisbon Humberto Delgado Airport', 'Lisbon', 'Portugal', 'LIS', 38.7812, -9.1348),
(55, 'Sydney Kingsford Smith International Airport', 'Sydney', 'Australia', 'SYD', -33.9399, 151.1753),
(56, 'Milan Malpensa Airport', 'Milan', 'Italy', 'MXP', 45.6300, 8.7220),
(57, 'Cairo International Airport', 'Cairo', 'Egypt', 'CAI', 30.1219, 31.4050),
(58, 'Amman Queen Alia International Airport', 'Amman', 'Jordan', 'AMM', 31.7222, 35.9933),
(59, 'Abu Dhabi International Airport', 'Abu Dhabi', 'UAE', 'AUH', 24.4333, 54.6497),
(60, 'Geneva International Airport', 'Geneva', 'Switzerland', 'GVA', 46.2381, 6.1083),
(61, 'Bucharest Henri Coandă International Airport', 'Bucharest', 'Romania', 'OTP', 44.5722, 26.1025),
(62, 'Athens Eleftherios Venizelos Airport', 'Athens', 'Greece', 'ATH', 37.9364, 23.9445),
(63, 'Zürich Airport', 'Zürich', 'Switzerland', 'ZRH', 47.4647, 8.5492),
(64, 'Frankfurt am Main International Airport', 'Frankfurt', 'Germany', 'FRA', 50.1109, 8.6821),
(65, 'Kuala Lumpur International Airport', 'Kuala Lumpur', 'Malaysia', 'KUL', 2.7456, 101.7213),
(66, 'King Khalid International Airport', 'Riyadh', 'Saudi Arabia', 'RUH', 24.9595, 46.6980),
(67, 'Abu Dhabi International Airport', 'Abu Dhabi', 'UAE', 'AUH', 24.4333, 54.6497),
(68, 'Istanbul Sabiha Gökçen International Airport', 'Istanbul', 'Turkey', 'SAW', 40.8987, 29.3095),
(69, 'Bahrain International Airport', 'Manama', 'Bahrain', 'BAH', 26.2711, 50.6367),
(70, 'Chennai International Airport', 'Chennai', 'India', 'MAA', 12.9987, 80.1718),
(71, 'Dhaka Hazrat Shahjalal International Airport', 'Dhaka', 'Bangladesh', 'DAC', 23.8431, 90.3974),
(72, 'Doha Hamad International Airport', 'Doha', 'Qatar', 'DOH', 25.2764, 51.5650),
(73, 'Copenhagen Kastrup Airport', 'Copenhagen', 'Denmark', 'CPH', 55.6176, 12.6243),
(74, 'Stockholm Arlanda Airport', 'Stockholm', 'Sweden', 'ARN', 59.6519, 17.9186),
(75, 'Helsinki-Vantaa Airport', 'Helsinki', 'Finland', 'HEL', 60.3191, 24.9630),
(76, 'Bucharest Henri Coandă International Airport', 'Bucharest', 'Romania', 'OTP', 44.5722, 26.1025),
(77, 'Warsaw Chopin Airport', 'Warsaw', 'Poland', 'WAW', 52.1654, 20.9671),
(78, 'Algiers Houari Boumediene Airport', 'Algiers', 'Algeria', 'ALG', 36.6925, 3.2153),
(79, 'Jakarta Soekarno-Hatta International Airport', 'Jakarta', 'Indonesia', 'CGK', -6.1256, 106.6559),
(80, 'Riyadh King Khalid International Airport', 'Riyadh', 'Saudi Arabia', 'RUH', 24.9595, 46.6980),
(81, 'Vienna International Airport', 'Vienna', 'Austria', 'VIE', 48.1140, 16.5695),
(82, 'Bengaluru Kempegowda International Airport', 'Bengaluru', 'India', 'BLR', 13.1974, 77.7062),
(83, 'Düsseldorf Airport', 'Düsseldorf', 'Germany', 'DUS', 51.2890, 6.7669),
(84, 'Cape Town International Airport', 'Cape Town', 'South Africa', 'CPT', -33.9650, 18.6019),
(85, 'Phuket International Airport', 'Phuket', 'Thailand', 'HKT', 8.1136, 98.3061),
(86, 'Bangalore Kempegowda International Airport', 'Bangalore', 'India', 'BLR', 13.1974, 77.7062),
(87, 'Singapore Changi Airport', 'Singapore', 'Singapore', 'SIN', 1.3644, 103.9915),
(88, 'Prague Václav Havel Airport', 'Prague', 'Czech Republic', 'PRG', 50.0895, 14.4433),
(89, 'Seoul Gimpo International Airport', 'Seoul', 'South Korea', 'GMP', 37.5575, 126.7923),
(90, 'Dubai World Central Airport', 'Dubai', 'UAE', 'DWC', 25.2532, 55.3657),
(91, 'Osaka Itami Airport', 'Osaka', 'Japan', 'ITM', 34.8125, 135.4389),
(92, 'Las Vegas McCarran International Airport', 'Las Vegas', 'USA', 'LAS', 36.0800, -115.1523),
(93, 'Boston Logan International Airport', 'Boston', 'USA', 'BOS', 42.3656, -71.0096),
(94, 'Mexico City Benito Juárez International Airport', 'Mexico City', 'Mexico', 'MEX', 19.4363, -99.0719),
(95, 'Helsinki-Vantaa Airport', 'Helsinki', 'Finland', 'HEL', 60.3191, 24.9630),
(96, 'Bangalore Kempegowda International Airport', 'Bangalore', 'India', 'BLR', 13.1974, 77.7062),
(97, 'Madrid–Barajas Adolfo Suárez Airport', 'Madrid', 'Spain', 'MAD', 40.4722, -3.5600),
(98, 'Singapore Changi International Airport', 'Singapore', 'Singapore', 'SIN', 1.3644, 103.9915),
(99, 'Auckland International Airport', 'Auckland', 'New Zealand', 'AKL', -37.0084, 174.7850),
(100, 'Porto Airport', 'Porto', 'Portugal', 'OPO', 41.2424, -8.6813);